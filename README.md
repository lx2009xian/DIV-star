# DIV* measurement

The python code of diversity measurement proposed by Loet Leydesdorff


In 2019, Loet Leydesdorff proposed a new measurement for diversity, and then Ronald Rousseau improved this measurement.

The new diversity of given paper can be described as:

<img src="https://latex.codecogs.com/svg.image?DIV*=n*(1-Gini)*\sum_{i=1,j=1}^{i=n,j=n}\tfrac{dij}{n*(n-1)}" title="DIV*=n*(1-Gini)*\sum_{i=1,j=1}^{i=n,j=n}\tfrac{dij}{n*(n-1)}" />

where n is the number of non-empty cells of given paper, Gini means the gini index of given paper and dij is the distance of cell i and j(Here, we use (1-cosine) as the distance measurement)(Ref:10.1016/j.joi.2019.03.016)
