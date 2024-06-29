import { foodApi } from "@apis/food";
import ClientProductList from "./ProductList.client";
import { ProductsAndNutritions } from "./ProductList.define";

interface Props {
  selectedFoodCategoryKey?: string;
  initialSelectedBrands?: string;
}

export default async function ProductList(props: Props) {
  const { selectedFoodCategoryKey, initialSelectedBrands } = props;

  if (!selectedFoodCategoryKey) return <>음식 카테고리를 선택해주세요.</>;

  const products = (await foodApi.getProducts(selectedFoodCategoryKey, initialSelectedBrands))
    .results;

  if (products.length === 0) return <>음식 데이터가 존재하지 않습니다.</>;

  const productIds = products.map((product) => product.id);
  const nutritions = await foodApi.getNutritions(productIds);
  const initialProductsAndNutritions: ProductsAndNutritions = products.map((product, index) => [
    product,
    nutritions[index],
  ]);

  return (
    <ClientProductList
      selectedFoodCategoryKey={selectedFoodCategoryKey}
      initialProductsAndNutritions={initialProductsAndNutritions}
    />
  );
}
