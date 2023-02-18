$("document").ready(() => {
  const BASE_URL = "http://127.0.0.1:5000/api/cupcakes";

  const $addBtn = $(".add-btn");
  const $getBtn = $(".get-cupcakes");

  $addBtn.on("click", handleAddClick);
  $getBtn.on("click", handleGetClick);

  async function handleGetClick(e) {
    e.preventDefault();
    const cupcakes = await getCupcakes();
    renderCupcakes(cupcakes);
  }

  async function handleAddClick(e) {
    e.preventDefault();
    createCupcake();
    const cupcakes = await getCupcakes();
    renderCupcakes(cupcakes);
  }

  async function getCupcakes() {
    // Gets cupcakes and returns result
    res = await axios.get(BASE_URL);
    res = res.data.cupcakes;
    return res;
  }

  function renderCupcakes(res) {
    const $ul = $("ul");
    for (item of res) {
      const $li = $("<li>");
      $li.text(
        `ID: ${item.id} is a ${item.flavor} flavored cupcake. It's ${item.size} in size and has a ${item.rating} rating.`
      );
      $ul.append($li);
    }
  }

  async function createCupcake() {
    const flavor = $("#flavor");
    const size = $("#size");
    const rating = $("#rating");
    const image = $("#image");
    const cupCakeData = {
      flavor: flavor.val(),
      size: size.val(),
      rating: rating.val(),
      image: image.val(),
    };
    flavor.val("");
    size.val("");
    rating.val("");
    image.val("");
    res = await axios.post(BASE_URL, cupCakeData);
    return res.data.cupcake;
  }
});
