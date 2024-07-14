import Checkbox from "@mui/material/Checkbox";
import { useCompareStore } from "@stores/compareStore";
import { COLOR } from "@defines/css";
import { ProductDetailResult } from "@apis/food.define";
import ProductCardTable from "./ProductCardTable";
import styles from "./ProductCard.module.css";

interface Props {
  productNutrition: ProductDetailResult;
}

export default function ProductCard(props: Props) {
  const { productNutrition } = props;
  const nutrition = productNutrition.nutritions[0];

  const { isComparing, selectedProducts, toggleSelectedProduct } = useCompareStore();

  return (
    <div className={styles.productCardWraper}>
      {isComparing && (
        <div className={styles.left}>
          <Checkbox
            sx={{
              color: COLOR.ORANGE_DARK,
              "&.Mui-checked": {
                color: COLOR.ORANGE_DARK,
              },
            }}
            onChange={() => toggleSelectedProduct(productNutrition.id)}
            checked={selectedProducts.includes(productNutrition.id)}
          />
        </div>
      )}
      <div className={styles.right}>
        <div className={styles.details}>
          <div>
            <p className={styles.productName}>
              {`${productNutrition.brand_name} - ${productNutrition.product_name}`}
            </p>
            <p className={styles.productBriefInfo}>
              {`${nutrition.data.serving_size}${nutrition.data.serving_unit} 당 ${nutrition.data.calories}kcal`}
            </p>
          </div>
          <div className={styles.imageDatails}>
            <div>원재료명</div>
            <div>영양성분표</div>
          </div>
        </div>
        <ProductCardTable nutrition={nutrition} />
      </div>
    </div>
  );
}
