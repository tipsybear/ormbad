# ORMBad

[![Build Status][travis_img]][travis_url]
[![Coverage Status][coverage_img]][coverage_url]
[![Stories in Ready][waffle_img]][waffle_url]

[![Cleaning up Waders mess][lego_troopers.jpg]][lego_troopers_flickr]

**Why use an ORM when you can just use straight up SQL in Python?**

## About

Object Relational Mappers (ORMs) seem like very useful tools, but unfortunately they can be tricky. Authors like [@codinghorror](https://twitter.com/codinghorror) and [@martinfowler](https://twitter.com/martinfowler) have given ORMs the fair shake in [_Object-Relational Mapping is the Vietnam of Computer Science_](http://blog.codinghorror.com/object-relational-mapping-is-the-vietnam-of-computer-science/) and [_OrmHate_](http://martinfowler.com/bliki/OrmHate.html) (seriously, even with those titles). It seems like such a good idea, but adding them to your programs is not trivial.

The thing is, SQL is a really great tool also. Once you learn SQL and know how to avoid SQL-Injection attacks, it turns out that using straight SQL via Python in a driver is a _joy_. The question should not be: how do we manage objects whose storage layer is a database? The question should be, how do we manage reusable SQL strings in our applications. Hence we set out to write this tool.

### Attribution

The image used in this README, [Cleaning up Waders mess][lego_troopers_flickr] by [Kristina Alexanderson](https://www.flickr.com/photos/kalexanderson/), is licensed under [CC BY-NC-ND 2.0](https://creativecommons.org/licenses/by-nc-nd/2.0/).


<!-- References -->

[lego_troopers.jpg]: docs/images/lego_troopers.jpg
[lego_troopers_flickr]: https://flic.kr/p/awJdiL
[travis_img]: https://travis-ci.org/tipsybear/ormbad.svg
[travis_url]: https://travis-ci.org/tipsybear/ormbad
[coverage_img]: https://coveralls.io/repos/tipsybear/ormbad/badge.svg?branch=master&service=github
[coverage_url]: https://coveralls.io/github/tipsybear/ormbad?branch=master
[waffle_img]: https://badge.waffle.io/tipsybear/ormbad.png?label=ready&title=Ready
[waffle_url]: https://waffle.io/tipsybear/ormbad
