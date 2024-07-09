import { foodApi } from "@apis/food";
import ClientProductList from "./ProductList.client";

interface Props {
  selectedFoodCategoryKey?: string;
  initialSelectedBrands?: string[];
}

export default async function ProductList(props: Props) {
  const { selectedFoodCategoryKey, initialSelectedBrands } = props;

  if (!selectedFoodCategoryKey) return <>음식 카테고리를 선택해주세요.</>;

  const { results: initialProductsNutritions, count } = await foodApi.getProductNutritions(
    selectedFoodCategoryKey,
    initialSelectedBrands
  );
  if (initialProductsNutritions.length === 0) return <>음식 데이터가 존재하지 않습니다.</>;

  return (
    <ClientProductList
      selectedFoodCategoryKey={selectedFoodCategoryKey}
      initialProductsNutritions={initialProductsNutritions}
      maxPage={Math.ceil(count / 10)}
    />
  );
}
