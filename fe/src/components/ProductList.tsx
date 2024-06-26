import ProductCard from "./product-card/ProductCard";
import { NutritionRs, ProductRs } from "@apis/food.define";
import { foodApi } from "@apis/food";
import styles from "./ProductList.module.css";

interface Props {
  selectedFoodCategoryKey?: string;
}

export default async function ProductList(props: Props) {
  const { selectedFoodCategoryKey } = props;

  if (!selectedFoodCategoryKey) return <>음식 카테고리를 선택해주세요.</>;

  const products = await foodApi.getProducts(selectedFoodCategoryKey);

  if (products.length === 0) return <>음식 데이터가 존재하지 않습니다.</>;

  const productIds = products.map((product) => product.id);
  const nutritions = await foodApi.getNutritions(productIds);
  const productsAndNutritions: [ProductRs, NutritionRs][] = products.map((product, index) => [
    product,
    nutritions[index],
  ]);

  return (
    <div className={styles.productListWrapper}>
      {productsAndNutritions.map(([product, nutrition]) => (
        <ProductCard product={product} nutrition={nutrition} />
      ))}
    </div>
  );
}
