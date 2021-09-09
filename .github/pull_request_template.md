# Checklist

- [ ] verision number is updated or the package is new
- [ ] project contains a valid license, specifically Apache v2.0.
- [ ] project passes all sonar and coverity checks
- [ ] project uploaded to the testpypi server using upload2testpypi label to trigger an upload
- [ ] approval from code owners

Once all 5 of these tasks have been completed, the pr is ready to be merged and pushed to the pypi server.

:memo: __NOTE if this PR contains changes that do not require a package update such as a modification to documentation or workflow files then label the PR 'non-release' to skip all these checks and avoid uploading a new change to the package server__
