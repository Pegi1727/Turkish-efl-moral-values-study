# Statistical Methods

## Notation and estimand
For one binary category of a categorical item, let `n` be the number of valid observations for that item and `x` the count in the category, with `0 ≤ x ≤ n` and `n > 0`. The observed proportion is `p̂ = x/n`. For a multi-category item, compute this separately for each category using the item-specific valid denominator; category proportions sum to one only when categories are mutually exclusive and exhaustive and share the same denominator. The independent units for teacher and student summaries are respondents within their respective cohorts. The cohorts themselves are not paired.

## Proportion standard error
The plug-in binomial standard error of an observed proportion is

`SE(p̂) = sqrt[p̂(1 − p̂) / n]`.

It is expressed on the proportion scale; multiply by 100 for percentage points. It is zero at `p̂=0` or `p̂=1`, which reflects the plug-in variance estimate, not certainty about the underlying population proportion. This formula describes sampling precision under a binomial/random-sampling model. With purposive sampling, it is best treated as a model-based descriptive precision measure, not evidence that the sample is representative or that population generalization is warranted. It does not account for clustering, weighting, nonresponse, measurement error, or design effects.

## Two-sided Wilson score 95% confidence interval
Let `z = Φ⁻¹(0.975) ≈ 1.959964` for a two-sided 95% interval. The Wilson score interval without continuity correction is

`D = 1 + z²/n`

`C = [p̂ + z²/(2n)] / D`

`H = [z / D] × sqrt[p̂(1−p̂)/n + z²/(4n²)]`

`CI_W = [C−H, C+H]`.

Equivalent lower and upper forms are

`L,U = {p̂ + z²/(2n) ± z sqrt[p̂(1−p̂)/n + z²/(4n²)]} / (1 + z²/n)`.

The interval is reported on the proportion scale (multiply endpoints by 100 for percent). It is bounded within `[0,1]` and generally performs better than the symmetric Wald interval for modest sample sizes or proportions near 0/1.

### Boundary behavior at 100% (and 0%)
For `x=n`, `p̂=1`, but the Wilson upper endpoint is **1**, not a degenerate zero-width `[1,1]` interval; the lower endpoint is `1/(1+z²/n)`, below one for finite `n`. For `x=0`, the lower endpoint is 0 and the upper endpoint is `z²/(n+z²)`, above zero. Thus a 100% observed sample proportion does not establish a 100% population proportion. At `n=50`, `x=50`, the interval is approximately `[0.9287, 1.0000]` (92.87%–100%); for `x=0`, it is approximately `[0, 0.0713]`. These are model-based intervals and do not correct purposive-sampling limitations.

## Descriptive analysis rationale
The raw data are small, categorical, and largely single-response. Counts and percentages are therefore transparent primary summaries. Standard errors and Wilson intervals communicate approximate binomial precision while avoiding the poor boundary behavior of Wald intervals. No hypothesis tests, regression, causal estimation, scale means, or paired teacher–student statistics are justified by the supplied design and schema. Cross-cohort contrasts are descriptive only; each proportion has its own denominator and interval. Qualitative narrative coding complements the categorical summaries by describing reported content; it cannot be converted into evidence of internalization or behavioral impact.

## Reproducible implementation (Python)
```python
from math import sqrt
from statistics import NormalDist

def proportion_se(x, n):
    if n <= 0 or not (0 <= x <= n):
        raise ValueError("Require n > 0 and 0 <= x <= n")
    p = x / n
    return sqrt(p * (1 - p) / n)

def wilson95(x, n):
    if n <= 0 or not (0 <= x <= n):
        raise ValueError("Require n > 0 and 0 <= x <= n")
    z = NormalDist().inv_cdf(0.975)
    p = x / n
    d = 1 + z*z/n
    c = (p + z*z/(2*n))/d
    h = z*sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c-h, c+h
```

Validate `wilson95(50,50)` has upper endpoint 1 and lower endpoint less than 1; validate `wilson95(0,50)` has lower endpoint 0 and upper endpoint greater than 0. Check category count totals and denominators before presenting intervals. Keep precision internally and round for display only.
