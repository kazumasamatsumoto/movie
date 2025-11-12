# #359 "Examples of ?."

Shikoku Metan: "Let's look at concrete ?. use cases."
Zundamon: "Handling API responses with response?.data?.name ?? 'Unknown' is neat!"
Shikoku Metan: "Yes, and it reaches nested values like profile avatars."
Zundamon: "DOM events can use element?.addEventListener safely?"
Shikoku Metan: "Exactly, listeners are added only when the element exists."
Zundamon: "Can we traverse product?.variants?.[0]?.pricing?.amount too?"
Shikoku Metan: "Of course; ?. returns undefined as soon as a link in the chain is missing."
Zundamon: "I'll lean on ?. whenever I need to read deep data with confidence!"

---

## 📺 Code for Display

```typescript
/** Example 1: Handling an API response */
const response = await fetchUser(id);
const userName = response?.data?.name ?? "Unknown";
const avatar = response?.data?.profile?.avatar;

/** Example 2: Using it in an event handler */
element?.addEventListener("click", () => {
  console.log(element?.dataset?.id);
});

/** Example 3: Complex data structures */
const price = product?.variants?.[0]?.pricing?.amount ?? 0;
const rating = reviews?.[0]?.rating?.average?.toFixed(1);
```
