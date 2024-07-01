import { ProductNutritionResult } from "@apis/food.define";
import ProductCardTable from "./ProductCardTable";
import styles from "./ProductCard.module.css";

interface Props {
  productNutrition: ProductNutritionResult;
}

export default function ProductCard(props: Props) {
  const { productNutrition } = props;
  const nutrition = productNutrition.nutritions[0];

  return (
    <div className={styles.productCardWraper}>
      <div className={styles.left}>
        <p className={styles.productName}>
          {productNutrition.brand_name} - {productNutrition.product_name}
        </p>
        <div className={styles.nutritionTable}>
          <p>{`${nutrition.data.serving_size}${nutrition.data.serving_unit} 당`}</p>
          <ProductCardTable nutrition={nutrition} />
        </div>
      </div>
    </div>
  );
}
