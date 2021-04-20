# How to Contribute

## Table of contents

* [Introduction](#introduction)
* [Forking, Branching and Committing Code](#forking-branching)
* [Writing Commit Messages](#writing-commit-messages)
* [Coding Style and Naming conventions](#coding-style-and-naming-conventions)
    * [Coding Style](#coding-style)
    * [Naming Conventions](#naming-conventions)
* [Commenting](#commenting)
* [Pull Requests](#pull-requests)
* [Resources](#resources)

## <a id="introduction"></a>Introduction

**First, Welcome!**

There are many ways you can help contribute to this project. Contributing
code, writing documentation, reporting bugs, as well as reading and providing
feedback on issues and pull requests. All are valid and necessary ways to help.
Any contribution, even the smallest, is welcome, so please join!

The purpose of this guide is to help you make well-formed contributions. While the rules established here
might look overwhelming to beginners, they are all pretty standard and reflect good practices
within the python coding world. The time you will spend understanding and applying them will likely 
help you everywhere, so don't hesitate spending time mastering them!

## <a id="forking-branching"></a>Forking, Branching and Committing Code

To develop this app we are using gitHub as distributed versioning control system.

We recommend that you first [fork this repository](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) 
to your own gitHub. When you are ready to work on a bug or a new feature, create yourself a new branch. 
This is important as it allows you to commit as often you like, while offering you the possibility to squash down your 
commits for more clarity before submitting a pull request (more about this in the "Pull Requests" section).

Please remember to commit frequently and focus each commit on a very specific piece of work, containing only related 
changes. If you need to use 'and' in your commit message, then you are probably grouping unrelated changessu
By doing so, you will greatly help other contributors understand the development process of the code.

When you are ready, you can ask to merge in the changes.

The workflow would look like this:

    git checkout -b your-task
    ... fix and git commit often ...
    git push origin your-task

You can then send us a pull request for the fix/feature you have worked on. Then we can
easily review it and merge it when ready (more on this in the last section).

## <a id="writing-commit-messages"></a>Writing Commit Messages

Writing a good commit message makes it simple for us to identify what your
commit does from a high-level. There are some basic guidelines we'd like you to follow.

A commit message should be structured in three parts (title, body, footer), each part separated by a blank line:

    type: Subject 
    
    body (optional) 
    
    footer (optional) 

### Title
The **title** (the first line) must be kept as short and sweet as possible. It *should not exceed 55 characters* 
(type + about 50 characters for the subject). This line is important because when git shows commits and it has 
limited space or a different formatting option is used the first line becomes all someone might see. This title 
should be composed of the type and the subject.

The **type** is contained within the title and aims at quickly indicating what the commit is about. It can be one of 
these types:
* `feat`: A new feature
* `fix`: A bug fix
* `docs`: Changes to documentation
* `style`: Formatting, missing semi-colons, etc; no code change
* `refactor`: Refactoring production code
* `test`: Adding tests, refactoring test; no production code change
* `chore`: Updating build tasks, package manager configs, etc; no production code change 

The **subject** should be written with an imperative tone to describe what a commit does, rather than what it did.
For example, use "change"; not "changed" or "changes". The best way to come up with a commit subject is to finish this phrase, 
"This commit will...". However you finish that phrase, use *that* as your commit message. 

### Body
If your change isn't something trivial or if the reasoning behind the change is not obvious, 
then please write up an extended message (**body**) explaining the fix, your rationale, 
and anything else relevant for someone else that might be reviewing the change.
Each line in the body should not be longer than 72 character, so that it can be displayed properly in 
the majority of tools.
Finally, make sure that there is a blank line between the title and the body, or your message might not display
properly when using git commands such as `log`, `shortlog` or `rebase` and other tools.

### Footer
Lastly, if there is a corresponding issue in Github issues for it, use the final line (**footer**)
to provide a message that will link the commit message to the issue and auto-close it if appropriate.

    feat: Summarize changes in around 50 characters or less 

    More detailed explanatory text, if necessary. Wrap it to about 72
    characters or so. In some contexts, the first line is treated as the
    subject of the commit and the rest of the text as the body. 

    Explain the problem that this commit is solving. Focus on why you
    are making this change as opposed to how (the code explains that).
    Are there side effects or other unintuitive consequences of this
    change? Here's the place to explain them. 

    Further paragraphs come after blank lines.
     - Bullet points are okay, too
     - Typically a hyphen or asterisk is used for the bullet, preceded
       by a single space

    If your commit is linked to an issue in the project gitHub issues, 
    put references to them at the bottom, like this:

    Resolves: #123  
    See also: #456, #789

## <a id="coding-style-and-naming-conventions"></a>Coding style and naming conventions

When writing code, please keep our style and naming convention in mind, which follow 
[PEP8](http://www.python.org/dev/peps/pep-0008/), unless explicitly stated.

### <a id="coding-style"></a>Coding Style

* PEP8 tries to keep line length at 79 characters. We follow it when we can, but not when it makes 
  a line harder to read. It is okay to go a bit over 79 characters if it improves readability.
* Before pushing your changes, please run [flake8](https://flake8.pycqa.org/en/latest/index.html#quickstart), it is a 
great tool to identify style mistakes. By doing so, you will help the reviewer of your code to focus on the logic of 
your code rather than the style. Using an IDE such as PyCharm, which control the style, can really help you correct 
these style mistake as you code, and will help you avoid having to make a lot of boring change before a commit.
* Use four space hanging indentation rather than vertical alignment:
  
      raise AttributeError(
        'Here is a multiline error message '
        'shortened for clarity.'
      )
  rather than:
  
      raise AttributeError('Here is a multiline error message '
                           'shortened for clarity.')

* Use single quotes for strings and double quotes if the string contains a single quote. However, don't spend
time doing unrelated refactoring of existing code to conform with this requirement.
* Blank lines should contain no whitespace.
* Imports are grouped specifically and ordered alphabetically. This is shown
  in the example below:
  
      # first set of imports are stdlib imports
      # non-from imports go first then from style import in their own group
      import csv
    
      # second set of imports are Django imports with contrib in their own
      # group.
      from django.contrib.auth.models import User
      from django.core.urlresolvers import reverse
      from django.db import models
      from django.utils import timezone
      from django.utils.translation import ugettext_lazy as _
    
      # third set of imports are external apps (if applicable)
      from tagging.fields import TagField
    
      # fourth set of imports are local apps
      from .fields import MarkupField

* Imports which are not used should be removed, unless they are needed for backward compatibility. In this case,
  add `# noqa` at the end of the import line so that flake8 does not report an error.
* Always use `reverse` and never `@models.permalink`.
* Tuples should be reserved for positional data structures and not used
  where a list is more appropriate.
  
### <a id="naming-conventions"></a>Naming Conventions

Here again, naming conventions are taken from PEP8.
* **Package and modules names** should use all-lowercases names and should be kept as short as possible. The use of underscore
should be avoided as much as possible.
* **Class names** should use UpperCamelCase convention and must depict the primary function of the 
class for readability. 
* **Exceptions** being classes, they follow the same naming convention as Classes and should end with 
  the suffix "Error".
* **Functions, methods and variables names** should be lowercase, with words separated by underscores if necessary, to
improve readability. They must describe accurately their content / purpose.
* **Constants** should be declared at module level, after imports, and should their name should be fully
capitalized.

## <a id="commenting"></a>Commenting

Documenting and commenting code properly is almost as important as writing good quality code. You have probably 
been in a situation where you had to dive into code written by somebody else, without comments or documentation,
or even in a situation where you are looking at old code you wrote more than a year ago, and wonder "what
is going on here." Proper documentation and comments aim at avoiding such a situation, and will help reviewers or
other contributors understand what is going on, how the overall goal of the code is achieved, and why the code
has been developed that way (more interesting readings on this topic in the "resources" section below).

The code you write has two primary audience: users and developers (you included).
As a general rule of thumb, commenting will target developers. In conjunction with well written code, comments 
help the reader better understand your code, its purpose, and design.
Documenting code, in the other hand, is describing its use and functionality to your users (obviously it also helps
contributors new to the project understand what the code is about and trying to achieve).

This section provides guidelines to guarantee good quality comments and documentations. If you are new to commenting
and documenting, [Documenting Python Code: A complete Guide](https://realpython.com/documenting-python-code/) is a 
great place to start learning more.
* Docstrings should be used to document the code. Classes and methods, functions, module, packages should all have
dedicated docstrings, located right after the `def` line.
  * The docstring for a **module** should list the classes, exceptions and functions (and any other objects) that are 
    exported by the module, with a one-line summary of each. (These summaries generally give less detail than the 
    summary line in the object's docstring.)
  * The docstring for a **class** should summarize its behavior and list the public methods and instance variables. 
    If the class is intended to be subclassed, and has an additional interface for subclasses, this interface should 
    be listed separately (in the docstring). 
  * The docstring for a **function** or **method** summarizes its behavior and document its arguments, return value(s), 
    side effects, exceptions raised, and restrictions on when it can be called (all if applicable). Optional 
    arguments should be indicated. It should be documented whether keyword arguments are part of the interface.
* Comments with # should be used for comments on variables, computations or operations within a function or method.
* The recommendations provided in [PEP257](https://www.python.org/dev/peps/pep-0257/) should be followed when 
  writing docstrings.
* The format of the docstring used for this project is inspired from **reStructured Text**. Each parameter 
  (for example `param_name`) in a function/method should be detailed using `:param param_name:`, to explain what the 
  parameter refers to. An example is provided below.
* Python **type hinting** should be used. It provides a complement to using docstring to provide information 
  about parameters. This helps IDEs to provide better code completion and allow the use of dedicated tools
  to detect possible issues, when a type is wrong. It also helps build and maintain a cleaner architecture. 
  An example is provided below.
* Since we are using type hinting, we DO NOT specify parameters' types in the docstring, and 
  `:type param_name:` as well as `:rtype:` are not used. Only when type hinting cannot be used can these two tags 
  be included in the docstring.
* Below is an example of a proper function declaration using docstring and type hinting:
  
      def increase_salary(starting_salary: float, rating: float) -> float:
      """ Returns the salary increased by the rating's percentage.
      
      rating 1 - 2 no increase
      rating 3 - 4 increase 5%
      rating 4 - 6 increase 10%
    
      :param starting_salary: the starting salary to which the increase applies
      :param rating: the rating defining how much is the salary increase
      :returns: the new salary value, including the increase
      :raises ValueError: raises a ValueError exception when "rating" is not 
      in the right range
      """

## <a id="pull-requests"></a>Pull Requests

Once you are ready to submit to changes and additions, start with pushing your
commits from your local git to this project fork on your gitHub profile.

When this is done, you can create a pull request from your fork, to our upstream
repository. If this is new to you, 
[GitHub Docs provides great explanations](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork)
about how to make it happen.

Please keep your pull requests focused on one specific topic only. If you
have a number of contributions to make, then please send separate pull
requests. It is much easier on maintainers to receive small, focused,
pull requests, than it is to have a single large one that batches up a
lot of unrelated commits. Ideally, a pull request should contain 1-3 commits.

If you ended up making multiple commits for one, well-defined, logical change, 
please rebase into a single commit.

    git rebase -i HEAD~10  # where 10 is the number of commits back you need

This will pop up an editor with your commits and some instructions. You want
to squash commits down by replacing 'pick' with 's' to have it combined with
the commit before it. You can squash multiple ones at the same time.

When you save and exit the text editor where you were squashing commits, git
will squash them down and then present you with another editor with commit
messages. Choose the one to apply to the squashed commit (or write a new
one entirely.) Save and exit will complete the rebase. Use a forced push to
your own fork.

    git push -f

## <a id="resources"></a>Resources

* [PEP8 - Style Guide for Python Code](http://www.python.org/dev/peps/pep-0008/)
* [Documenting Python Code: A complete Guide](https://realpython.com/documenting-python-code/)
* [Code tells you how, Comments tell you why](https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/)
* [SO: What is the standard python docstring format?](https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format)
* [PEP257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
* [PEP484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
* [Python Type Checking Guide](https://realpython.com/python-type-checking/)