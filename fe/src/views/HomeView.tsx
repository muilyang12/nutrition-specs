import FoodCategorySelect from "@components/FoodCategorySelect";
import ProductList from "@components/ProductList";

export default function HomeView() {
  return (
    <>
      <FoodCategorySelect />
      <ProductList />
    </>
  );
}
