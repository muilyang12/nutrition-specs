import Checkbox from "@mui/material/Checkbox";
import { useModalStore } from "@stores/modalStore";
import { useCompareStore } from "@stores/compareStore";
import { COLOR } from "@defines/css";
import { ProductDetailResult } from "@apis/food.define";
import ProductCardNutritionModal from "./ProductCardNutritionModal";
import ProductCardIngredientModal from "./ProductCardIngredientModal";
import ProductCardTable from "./ProductCardTable";
import styles from "./ProductCard.module.css";

interface Props {
  productNutrition: ProductDetailResult;
}

export default function ProductCard(props: Props) {
  const { productNutrition } = props;
  const nutrition = productNutrition.nutritions[0];
  const ingredient = productNutrition.ingredients[0];

  const { isComparing, selectedProducts, toggleSelectedProduct } = useCompareStore();
  const { openModal } = useModalStore();

  const handleClickNutrition = () => {
    openModal(
      <ProductCardNutritionModal
        productName={productNutrition.product_name}
        s3Key={nutrition.s3_key}
      />
    );
  };

  const handleClickIngredient = () => {
    openModal(
      <ProductCardIngredientModal
        productName={productNutrition.product_name}
        s3Key={ingredient.s3_key}
        ingredientIds={ingredient.ingredients}
      />
    );
  };

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
            {nutrition?.s3_key && <div onClick={handleClickNutrition}>영양성분표</div>}
            {ingredient?.s3_key && <div onClick={handleClickIngredient}>원재료명</div>}
          </div>
        </div>
        <ProductCardTable nutrition={nutrition} />
      </div>
    </div>
  );
}
