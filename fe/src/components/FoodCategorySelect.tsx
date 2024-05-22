"use client";

import { useParams, useRouter } from "next/navigation";
import { useEffect, SyntheticEvent } from "react";
import Autocomplete from "@mui/material/Autocomplete";
import TextField from "@mui/material/TextField";
import { useFoodCategoriesStore } from "@stores/useFoodCategories";
import { FoodCategoryPageParams } from "@defines/params.define";
import { foodApi } from "@apis/food";
import { FoodCategoryRs } from "@apis/food.define";

export default function FoodCategorySelect() {
  const router = useRouter();
  const params = useParams<FoodCategoryPageParams>();
  const selectedFoodCategoryKey = params.foodCategory;

  const { foodCategories, setFoodCategories } = useFoodCategoriesStore();

  useEffect(() => {
    foodApi.getFoodCategories().then((result) => {
      setFoodCategories(result.map((category) => ({ ...category, label: category.category_name })));
    });
  }, []);

  const handleChangeValue = (_event: SyntheticEvent, value: FoodCategoryRs | null) => {
    if (value) router.push("/" + value.category_key);
  };

  return (
    <Autocomplete<FoodCategoryRs>
      disablePortal
      id="food-category-select"
      options={foodCategories}
      sx={{ width: 300 }}
      renderInput={(params) => <TextField {...params} label="음식 카테고리" />}
      onChange={handleChangeValue}
      autoHighlight
    />
  );
}
