import { NutritionRs, ProductRs } from "@apis/food.define";
import styles from "./ProductCard.module.css";

interface Props {
  product: ProductRs;
  nutrition: NutritionRs;
}

export default function ProductCard(props: Props) {
  const { product, nutrition } = props;

  console.log(nutrition.data);

  return (
    <div className={styles.productCardWraper}>
      <div className={styles.upper}>
        <div className={styles.left}>
          <p className={styles.leftProductName}>
            {product.brand_name} - {product.product_name}
          </p>
        </div>
        <div className={styles.right}></div>
      </div>
      <div className={styles.nutritionTable}>
        <p>{`${nutrition.data.serving_size}${nutrition.data.serving_unit} 당`}</p>
        <table className={styles.table}>
          <tbody>
            <tr>
              <td>탄수화물</td>
              <td>{`${nutrition.data.total_carbohydrate}g`}</td>
              <td>당류</td>
              <td>{`${nutrition.data.sugars}g`}</td>
            </tr>
            <tr>
              <td>단백질</td>
              <td>{`${nutrition.data.protein}g`}</td>
              <td>지방</td>
              <td>{`${nutrition.data.total_fat}g`}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
