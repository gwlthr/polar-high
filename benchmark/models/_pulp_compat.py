"""The expression and status APIs shared by PuLP 3.3.2 and 4.x."""

from pulp import HiGHS_CMD, LpMinimize, LpProblem, value

try:
    from pulp import LpSolveStatus, lpSum_vars, lpSum_vars_coefs

    LpStatusOptimal = LpSolveStatus.Optimal
except ImportError:
    from pulp import LpAffineExpression, LpStatusOptimal
    from pulp import lpSum as lpSum_vars

    # Both versions construct the objective directly from (variable, coefficient)
    # pairs, avoiding an intermediate expression for every coefficient product.
    lpSum_vars_coefs = LpAffineExpression

__all__ = [
    "HiGHS_CMD",
    "LpMinimize",
    "LpProblem",
    "LpStatusOptimal",
    "lpSum_vars",
    "lpSum_vars_coefs",
    "value",
]
