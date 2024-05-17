import { useEffect } from "react";
import { useSearchParams } from "react-router-dom";
import Autocomplete from "@mui/material/Autocomplete";
import TextField from "@mui/material/TextField";
import { useFoodCategoriesStore } from "../stores/useFoodCategories";
import { foodApi } from "../apis/food";

export default function FoodCategorySelect() {
  const [, setSearchParams] = useSearchParams();

  const { foodCategories, setFoodCategories } = useFoodCategoriesStore();

  useEffect(() => {
    foodApi.getFoodCategories().then(({ categories }) => {
      setFoodCategories(
        categories.map((category) => ({ ...category, label: category.category_name }))
      );
    });
  }, []);

  const handleChangeValue = (_event, value) => {
    if (value) setSearchParams({ "food-category": value.category_name });
    else setSearchParams((prev) => prev.delete("food-category"));
  };

  return (
    <Autocomplete
      disablePortal
      id="food-category-select"
      options={foodCategories}
      sx={{ width: 300 }}
      renderInput={(params) => <TextField {...params} label="음식 카테고리" />}
      onChange={handleChangeValue}
    />
  );
}
