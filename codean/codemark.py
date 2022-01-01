import logging
from pathlib import Path
from typing import Collection, Iterable

import pygit2

from .model import Codemark


def open_repository(path: Path) -> pygit2.Repository:
    if not path.is_dir():
        raise FileNotFoundError("Repository does not exist.")

    try:
        return pygit2.Repository(str(path))
    except Exception:
        logging.exception(f"Failed to open repository with id {id}")
        raise


def migrate_codemarks(
    path: Path | str,
    from_revision: str,
    to_revision: str,
    codemarks: Iterable[Codemark],
) -> Collection[Codemark]:
    if isinstance(path, str):
        path = Path(path)

    repository = open_repository(path)
    tree_from = repository.revparse_single(from_revision)
    tree_to = repository.revparse_single(to_revision)

    if tree_from.id == tree_to.id:
        raise ValueError(
            f"The from and to revision point to the same commit id {tree_from.id}"
        )

    # Calculate the difference between them
    patches = repository.diff(tree_from, tree_to)
    patches.find_similar()

    migrated_codemarks: list[Codemark] = []

    # Go through all patches
    for patch in patches:
        blob_old = patch.delta.old_file
        blob_new = patch.delta.new_file

        """ Taken from libgit2/include/git2/diff.h git_diff_line_t enum
        These are the possible values for the line.origin

        /* These values will be sent to `git_diff_line_cb` along with the line */
        GIT_DIFF_LINE_CONTEXT   = ' ',
        GIT_DIFF_LINE_ADDITION  = '+',
        GIT_DIFF_LINE_DELETION  = '-',

        GIT_DIFF_LINE_CONTEXT_EOFNL = '=', /**< Both files have no LF at end */
        GIT_DIFF_LINE_ADD_EOFNL = '>',     /**< Old has no LF at end, new does */
        GIT_DIFF_LINE_DEL_EOFNL = '<',     /**< Old has LF at end, new does not */
        """
        # Go through all patch hunks
        for hunk in patch.hunks:

            # Now we can finally go through all lines
            for line in hunk.lines:

                # We can skip all contextual lines
                if line.origin == " ":
                    continue

                # TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
                # You are up!
                # TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO

        # We grab all relevant codemarks (namely, the Codemarks placed in this file)
        relevant_codemarks = [
            c
            for c in codemarks
            if c.path == blob_old.path and c.hash == blob_old.id.hex
        ]

        # Now we can migrate all Codemarks
        # NOTE: If you can do this in one go or while going through the patches, go for it!
        for codemark in relevant_codemarks:

            # TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
            # You are up!
            # TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO

            # We create the new (migrated) Codemark
            migrated_codemark = Codemark(
                path=blob_new.path,
                hash=blob_new.id.hex,
                parent_id=codemark.id,
                description=codemark.description,
                start_line_number=codemark.start_line_number,  # TODO
                start_column=codemark.start_column,  # TODO
                end_line_number=codemark.end_line_number,  # TODO
                end_column=codemark.end_column,  # TODO
                # Can be used to indicate there was just no way to merge...
                # Try to place the Codemark as close as possible to where it probably
                # went!
                # merge_conflict_revision=to_revision,
            )
            migrated_codemarks.append(migrated_codemark)

    return migrated_codemarks
