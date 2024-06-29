import FoodCategorySelect from "@components/FoodCategorySelect";
import ProductList from "@components/product-list/ProductList.server";

export default function HomeView() {
  return (
    <>
      <FoodCategorySelect />
      <ProductList />
    </>
  );
}
