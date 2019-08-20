# A sample `.travis.yml` using `conda` on `linux`, `osx` and `windows`

## Description

* This file is intend to be a sample of `.travis.yml` file for the [Travis-CI](https://www.travis-ci.org).

### What is the CI ?

* CI here stands for [Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration)

* The Wikipedia describes as follows:
> ...**CI** is the practice of merging all developers' working copies to a shared mainline several times a day.

* To my understanding, when integrating a new work, the code base integrity must be confirmed.

* As CI may execute a number of tasks such as building, testing, and merging several times a day, certain level of automation is desirable.

* For example, [Jenkins](https://en.wikipedia.org/wiki/Jenkins_(software)), an [open source](https://github.com/jenkinsci/jenkins) project, can be employed to automate the CI/[CD](https://en.wikipedia.org/wiki/Continuous_delivery).

### What is the [Travis-CI.org](https://travis-ci.org)?

* Also from the Wikipedia:
> Travis-CI is a hosted CI service used to build and test software project hosted at GitHub.

* The company HQ is located in Berlin, Germany.

### What is the `.travis.yml` file?

* When a developer `git push`s to a Travis-CI-enabled GitHub repository, Travis-CI would build and test the software.

* Travis-CI would search for this `.travis-ci.yml` file at the root of the repository.

* This `.travis-ci.yml` file would describe the [procedures](https://docs.travis-ci.com) to build and test the software.

* `.yml` means [YAML format](https://en.wikipedia.org/wiki/YAML).

## Separate shell script files

* One possible way to simplify the `.travis.yml` file is to write several [shell script](https://linuxcommand.org/lc3_writing_shell_scripts.php) files describing subsections of the procedure : `before_install`, `install`, and `script`

* For example, to run a `my_before_install.sh` file, one may consider adding following lines to the `.travis.yml` file.

``` yaml
before_install:
  - . my_before_install.sh
```
