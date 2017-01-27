Within every release section, Collect changes in three sub-sections:

##### Breaking

These changes should be rather rare, as they are going to break
compatibility with some other software or previous installations, so
the user cannot just update to this version and expect that everything
will work without their intervention.

When a breaking change is listed, it should go with notes about what
needs to be done in order to successfully update to the new version
from a former one

##### New

These are new features or changes that have an impact on the user
experience, but are compatible with previous versions. Entries listed
here should not prevent the user from seamlessly update the software
without any adjustment

##### Internal

These are changes that cannot be observed by the user. Refactoring, or
fixing errors that were not reported yet

### In case it's not obvious

- Add lines just to the unreleased section. Released sections are
  supposed to be already distributed and cannot be changed anymore
