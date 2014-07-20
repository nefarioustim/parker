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
