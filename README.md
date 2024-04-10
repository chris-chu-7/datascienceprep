### Data Science Review

This is basically a data science repository to review certain topics. 

**Linear Regression**

For this algorithm, I utilized the Boston Housing Dataset where I attempted to find a correlation between the value of a Boston Home to the Crime Rate of the corresponding neighborhood. Define x̄ as the mean of x and ȳ as the the mean of y. Now we want to compute the slope α and the intercept β for the resulting equation expressed as

y = α * x + β.

Now we can have predefined value and we from equations can see that  α = Σ (all data points)((y - ȳ)(x - x̄))/(Σ (all data points)((x - x̄)^2)), which indicates the average of the slope, and that β = ȳ - α * x which is directly from the equation so in aggregate we can compute

β = ȳ - x * Σ (all data points)((y - ȳ)(x - x̄))/(Σ (all data points)((x - x̄)^2)).

After this we can plot the line of best fit and the scatterplot in the same graph using the matplotlib library and it seems like there's a negative correlation between crime rate and home value in Boston area. 
