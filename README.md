# Codean interview challenge

This repository contains a test suite and the beginning of our core algorithm used in the **Codean Review Environment (CRE)**.

So what does this core algorithm do? It automatically migrates manually placed Codemarks (annotations over source code) from one version of a text file to the next.

![Codemarks side-by-side](example-diff-codemarks.png)

What you see in the above screenshot of the CRE is a normal side-by-side diff of source code augmented with Codemarks. Each colored section in the left side of the screenshot is a Codemark and is manually placed by a security expert.

Because source code changes rapidly, we want to make sure that the Codemarks are automatically migrated to new versions of the source code. The manually placed Codemarks on the left side of the screenshot are "migrated" by an algorithm and automatically placed in the new file (right side of the screenshot). Some Codemarks are impossible to migrate because of changes to the source code. These Codemarks should be moved as close as possible to wherever they are probably relevant and marked with a merge conflict. This way, a human security expert can easily identify which Codemarks need manually review and fix them accordingly.

The migration of Codemarks is deceptively difficult and our current algorithm can always be improved. Hence, it makes for a great interview challenge. **Good luck!**

## The challenge

Your goal is to implement this algorithm in `codean/codemark.py` and test your solution using `python test.py`. This runs pytest on the tests defined in `tests` folder and uses additional test data from `test-codemarks.yaml`.

Please note that you should use patch information from Git first. If you have time to spare and you can improve the algorithm using pattern matching and other heuristics, go for it, but we do not expect you to do this.

P.S. You will need Python 3.9+ and a virtual environment. Use `virtualenv venv`, activate said virtual environment and `pip install -r requirements.txt` to get started!

### Bonus points

Feel free to improve ANYTHING you see that could be improved (pure bonus). Some ideas I had while working on this challenge:

-   [ ] 100% coverage is something we aim for, but it should serve its purpose.
-   [ ] Think the test cases can be better, go for it!
-   [ ] Add extra Codemarks, awesome!
-   [ ] Use [Poetry](https://python-poetry.org/) for dependency management.
-   [ ] Make changes to the example repository to make it more challenging for the algorithm you rock!
-   [ ] Use Mypy daemon with the pytest-mypy plugin for speedup (is this even possible?!).

**NOTE: No need to containerize this repository, that work is already done and you get no bonus points for that ;)**

### Things we care about at Codean

-   Readable and documented code, **use [Black](https://black.readthedocs.io/) for automatic formatting**.
-   Committing often and using [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).
-   Going full static typing with Mypy, YAY!
-   Writing tests is important!
-   Logging is better then print!
-   Early optimization is pure evil...
-   Being independent, but never stubborn, so ask help if you are stuck to prevent wasting time.

### test-repository.git

This the test repository in its bare form (`git clone --bare`). If you want to make changes to this test repository, or add file changes to test your algorithm you can run `git clone test-repository.git`.

Now you can make changes to in the `test-repository` folder and do your thing (`git commit -a --amend --no-edit` is your friend). After, you can run `git push` (`--force` probably) to put it back into the bare `test-repository.git`.

**TIP: Make sure to run `git gc --aggressive` within `test-repository.git` to pack it tight before committing to the interview challenge repository.**

## Reading materials

You may need to brush up you Python and/or Git skills. Feel free to do so, below you find relevant links to get you started on your search.

### Python

-   Make sure to use a language server for your IDE to make your life easier! https://github.com/python-lsp/python-lsp-server
-   **pygit2 documentation is really bad but you have to use it (probably) https://www.pygit2.org/**
-   **Understanding all of Python, through its builtins https://sadh.life/post/builtins/**
-   What is new in Python 3.10 https://docs.python.org/3/whatsnew/3.10.html
-   Getting started with Mypy https://mypy.readthedocs.io/en/stable/getting_started.html
-   TypedDict https://adamj.eu/tech/2021/05/10/python-type-hints-how-to-use-typeddict/ _(maybe pydantic models are better)_
-   Pydantic https://pydantic-docs.helpmanual.io/usage/mypy/
-   https://dropbox.tech/application/our-journey-to-type-checking-4-million-lines-of-python

### Git

-   On how git should track stuff by Linus: https://web.archive.org/web/20160206150253/http://article.gmane.org/gmane.comp.version-control.git/217
-   What is exactly stored: https://stackoverflow.com/questions/20666331/how-git-branches-and-tags-are-stored-in-disks/20800756#20800756
-   How do git commits actually look https://blog.thoughtram.io/git/2014/11/18/the-anatomy-of-a-git-commit.html
