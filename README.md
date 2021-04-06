# tasty-recipes-corpus

### About our project


We collected recipes from [Tasty website](https://tasty.co/). The elements we scraped include recipe title, description, ingredients, and preparation steps. We collected around 2000 recipes. However, due to limited budget, we were only able to annotate 800 of them. Our annotations are divided into five categories: Appetizer/side-dish, Main course, Dessert, Drinks, and Other.

We used Amazon Mechanical Turk annotate the recipes  based on tge categeries and for each recipe, we assign it to three different workers. Then, we extracted the best annotation if two annotators agree on one category. We investigated the inter-annotator agreement and we chose to use Krippendorff’s phi and alpha here because we have five categories(Appetizers/Side dish, Main course, Dessert, Drinks and Other). Based on Krippendorff’s alpha result, the observed disagreement is high (57.375%). The alpha is around 0.42, below the lowest conceivable limit (0.667), and falls into the range of (0.41, 0.6) as being moderate.

*This project is part of COLX 523 Corpus Linguistics class. Due to privacy policy of TASTY website, we are unable to include the scraped data here.*
