# Checklist

:memo: __NOTE This is a pull request from a fork. These do not have access to secrets so some of our status checks will not work. Admins please follow the below instructions to approve and move to a new pr able to access secrets__

- [ ] verify requested changes, make sure no workflow files have been changed
- [ ] if workflow files exist, a label updated-workflows will be added to the pr
- [ ] if no workflow files found, a label fork-tests-passed will be added to the pr
- [ ] if everything looks good, and fork-tests-passed label has been added, add label fork-approved and wait for pr to update base branch to fork-[0-9]+
- [ ] once the check has run, you should be able to merge into the fork-[0-9]+ branch