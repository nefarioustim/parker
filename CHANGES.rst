0.8.0
----------------------------------------

- Updated key-value functionality to allow a sub-selector to return
  a list of values.

- Added the ability to add an expiry time in seconds to the RedisSet
  objects, with a default of 5 days.

- Added an extra set to track URIs that are already on the crawl queue. This
  should hopefully cut down on duplication but may eat memory if there are
  multiple possiple URIs for the same page.

0.7.3
----------------------------------------

- Patch to fix an issue where the consumer was overlooking media URIs that start
  with / and are therefore relative to the base_uri configuration.

- Added boto to the requirements for future use.

0.7.2
----------------------------------------

- Patch to fix an issue where the crawler was overlooking URIs that start
  with / and are therefore relative to the base_uri configuration.

0.7.1
----------------------------------------

- Patch to fix an issue where, if class is not present in the site config, the
  path includes "None".

0.7.0
----------------------------------------

- Rework the client to allow for improved proxy failover should we
  need it. Improve testing a little to back this up.

- Add tagging to the configuration. These are simply passed through to the
  resulting JSON objects output by the model so that you can tag them with
  whatever you want.

- Add classification to the configuration. Again this is passed through, but
  is also used in the output file path from the consumer worker.

0.6.0
----------------------------------------

- Add tracking of visited URIs as well as page hashes to the
  crawl worker. Use that to reduce the number of URIs added to
  the crawl queue.

0.5.1
----------------------------------------

- Fix an issue with the order of key-value reference resolution
  that prevented the effective use of unique_field if using a
  field that was a kv_ref.

- Add some Parker specific configuration so we can specify where
  to download, in case the PROJECT env variable doesn't exist.

0.5.0
----------------------------------------

- Update ConsumeModel to post process the data. This enables us to
  populate specific data from a reference to a key-value field.

- Reorder changes so newest first, and rename to "Changes" in the
  long description.

0.4.2
----------------------------------------

- Bug fix to fix RST headers which may be the problem.

- Remove the decode/encode which is not the issue.

0.4.1
----------------------------------------

- Bug fix to see if RST in ASCII fixes issues on PyPI.

0.4.0
----------------------------------------

- Added handling for a PARKER_CONFIG environment variable, allowing
  users to specify where configuration files are loaded from.

- Added the ``parker-config`` script to install default configuration
  files to a passed location. Also prints out an example PARKER_CONFIG
  environment variable to add to your profile files.

- Updated documentation to use proper reStructuredText files.

- Add a CHANGES file to track updates.
