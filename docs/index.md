# Welcome to ORMBad

Object Relational Mappers (ORMs) seem like very useful tools, but unfortunately they can be tricky. Authors like [@codinghorror](https://twitter.com/codinghorror) and [@martinfowler](https://twitter.com/martinfowler) have given ORMs the fair shake in [_Object-Relational Mapping is the Vietnam of Computer Science_](http://blog.codinghorror.com/object-relational-mapping-is-the-vietnam-of-computer-science/) and [_OrmHate_](http://martinfowler.com/bliki/OrmHate.html) (seriously, even with those titles). It seems like such a good idea, but adding them to your programs is not trivial.

The thing is, SQL is a really great tool also. Once you learn SQL and know how to avoid SQL-Injection attacks, it turns out that using straight SQL via Python in a driver is a _joy_. The question should not be: how do we manage objects whose storage layer is a database? The question should be, how do we manage reusable SQL strings in our applications. Hence we set out to write this tool.
