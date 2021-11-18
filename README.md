# Open Source Project Summary

This repo is part of the NCR open source project. In order to publish changes to the package, you must go through the PR review process.

Code changes must pass several quality gates before they can be merged including:
 1. Coverity & Sonar scans
 2. License checks
 3. Updated version number

Once all these checks have passed, you must trigger a successful upload of the package to testpypi before the pr can be merged. Warning: further pushes to the branch after a successful testpypi upload will make this distinction stale. Additionally, the code must be approved by code owners. For more information on the steps, refer to the [pull request template](.github/pull_request_template.md).
