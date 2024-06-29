import { foodApi } from "@apis/food";
import ClientBrandFilter from "./BrandFilter.client";

interface Props {
  selectedFoodCategoryKey?: string;
}

export default async function BrandFilter(props: Props) {
  const { selectedFoodCategoryKey } = props;

  if (!selectedFoodCategoryKey) return <></>;

  const brands = await foodApi.getBrands(selectedFoodCategoryKey);

  return <ClientBrandFilter brands={brands} />;
}
