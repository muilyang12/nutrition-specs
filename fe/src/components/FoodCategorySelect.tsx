"use client";

import { useParams, useRouter } from "next/navigation";
import { useState, useEffect, SyntheticEvent } from "react";
import Autocomplete from "@mui/material/Autocomplete";
import TextField from "@mui/material/TextField";
import { FoodCategoryPageParams } from "@defines/params.define";
import { foodApi } from "@apis/food";
import { FoodCategoryRs } from "@apis/food.define";

export default function FoodCategorySelect() {
  const router = useRouter();
  const params = useParams<FoodCategoryPageParams>();
  const selectedFoodCategoryKey = params.foodCategory;

  const [options, setOptions] = useState<FoodCategoryRs[]>([]);

  useEffect(() => {
    foodApi.getFoodCategories().then((result) => {
      setOptions(result.map((category) => ({ ...category })));
    });
  }, []);

  const handleChangeValue = (_event: SyntheticEvent, value: FoodCategoryRs | null) => {
    if (value) router.push("/" + value.category_key);
  };

  return (
    <Autocomplete<FoodCategoryRs>
      disablePortal
      id="food-category-select"
      options={options}
      getOptionLabel={(option) => option.category_name}
      renderInput={(params) => <TextField {...params} label="음식 카테고리" />}
      onChange={handleChangeValue}
      sx={{ width: 300 }}
      autoHighlight
    />
  );
}
