import { NutritionRs, ProductRs } from "@apis/food.define";
import ProductCardTable from "./ProductCardTable";
import styles from "./ProductCard.module.css";

interface Props {
  product: ProductRs;
  nutrition: NutritionRs;
}

export default function ProductCard(props: Props) {
  const { product, nutrition } = props;

  return (
    <div className={styles.productCardWraper}>
      <div className={styles.left}>
        <p className={styles.productName}>
          {product.brand_name} - {product.product_name}
        </p>
        <div className={styles.nutritionTable}>
          <p>{`${nutrition.data.serving_size}${nutrition.data.serving_unit} 당`}</p>
          <ProductCardTable nutrition={nutrition} />
        </div>
      </div>
    </div>
  );
}
