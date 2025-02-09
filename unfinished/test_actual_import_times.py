import cProfile, pstats, os


def i_t():
    import minified_tge


def profile_function(function, filename: str, *inputs, **extra):
    """Profile a function and save performance stats to files."""

    profile = cProfile.Profile()
    profile.enable()

    return_ = function(*inputs, **extra)

    profile.disable()

    with open(f"{filename}.txt", "w") as f:
        stats = pstats.Stats(profile, stream=f)
        stats.sort_stats("cumulative")
        stats.print_stats()

    return return_


#import sys

# def is_tge_imported(message:str):
#     print(message, "tge" in sys.modules)

# is_tge_imported("Before testing")

profile_function(i_t, "profile.txt")
#is_tge_imported("After testing")


import minified_tge

print(minified_tge.INIT_TIME)
# python -v test.py > import_log.txt 2>&1