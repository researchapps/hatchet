#!/usr/bin/env python

import hatchet as ht


if __name__ == "__main__":
    # Path to caliper cali file.
    cali_file = "../../hatchet/tests/data/caliper-cali/caliper-ex.cali"

    # Setup desired cali query.
    grouping_attribute = "function"
    default_metric = "sum(sum#time.duration),inclusive_sum(sum#time.duration)"
    query = "select function,%s group by %s format json-split" % (
        default_metric,
        grouping_attribute,
    )

    # Use hatchet's ``from_caliper`` API with the path to the cali file and the
    # query. This API will internally run ``cali-query`` on this file to
    # produce a json-split stream. The result is stored into Hatchet's
    # GraphFrame.
    gf = ht.GraphFrame.from_caliper(cali_file, query)

    # Printout the DataFrame component of the GraphFrame.
    print(gf.dataframe)
    print("\n")

    # Printout the graph component of the GraphFrame. Specifically, enable
    # coloring, and only show those nodes with a positive ``time (inc)`` value.
    print(gf.tree(color=True, threshold=0.0, metric="time (inc)"))
