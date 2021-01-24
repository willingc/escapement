#!/usr/bin/env ruby
# usage:

#   ruby all-releases ipython jupyter jupyterlab jupyterhub

# dependencies:

# gem install netrc octokit activesupport faraday-http-cache

# attribution: minrk

require "rubygems"
require "octokit"
require "faraday-http-cache"
require "active_support"

# enable caching
stack = Faraday::RackBuilder.new do |builder|
  store = ActiveSupport::Cache::FileStore.new "#{Dir.pwd}/cache"
  builder.use Faraday::HttpCache, serializer: Marshal, store: store, shared_cache: false
  builder.use Octokit::Response::RaiseError
  builder.adapter Faraday.default_adapter
end


Octokit.auto_paginate = true
Octokit.middleware = stack
github = Octokit::Client.new(:netrc => true)

# csv header
puts "Date, Org, Repo, Version"

ARGV.each do |org_or_repo|
  if org_or_repo.include? '/'
    repos = [github.repo(org_or_repo)]
  else
    repos = github.repos(org_or_repo)
  end
  repos.each do |repo|
    tags = github.tags(repo.full_name)
    if not tags.empty?
      # human ouptut
      # puts "#{repo.full_name}: #{tags.length} releases"
    end
    tags.empty? or
    tags.each do |tag|
      v = tag.name
      # trim prefixes for old releases
      if v.start_with? 'rel-'
        v = v.slice(4, v.length)
      end
      if v.start_with? 'v'
        v = v.slice(1, v.length)
      end
      # exclude prereleases
      if v.match(/(b|a|rc|dev)\d*$/)
        # prerelease
        next
      end
      # exclude non-version tags (e.g. presentations for tutorials)
      if not v.match(/^\d+(\.\d+)*$/)
        # not a release
        next
      end
      commit = tag.commit.rels[:self].get.data.commit
      date = commit.committer.date
      # human output:
      # puts "  #{v}: #{date.strftime '%Y-%m-%d'}"
      # csv output:
      puts "#{date.strftime '%Y-%m-%d'}, #{repo.owner.login}, #{repo.name}, #{v}"
    end
  end
end
