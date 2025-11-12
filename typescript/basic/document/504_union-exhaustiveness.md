# #504 「Union型の網羅性」

四国めたん「Union型全般でも漏れを作りたくないよね。」
ずんだもん「Valueのprocess()はtypeofで全部の型をさばいてた。」
四国めたん「最後にconst exhaustive: never = valueと書けば網羅性が保証される。」
ずんだもん「AnimalのUnionはinstanceofでCatとDogを切り分けてたのだ。」
四国めたん「違う型ガードでもassertNever(animal)で締めておけば安心。」
ずんだもん「Directionのリテラル型もifチェーンで全部書いてたね。」
四国めたん「北南東西を全部処理した後にassertNever(direction)で見張る。」
ずんだもん「Union型ならどんなガードでも最後のneverチェックを忘れない。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: typeofガードで網羅 */
type Value = string | number | boolean;

function process(value: Value): string {
  if (typeof value === "string") {
    return value.toUpperCase();
  } else if (typeof value === "number") {
    return value.toString();
  } else if (typeof value === "boolean") {
    return value ? "true" : "false";
  }
  const exhaustive: never = value;
  return exhaustive;
}

/** Example 2: クラスUnionの処理 */
class Cat { meow() {} }
class Dog { bark() {} }
type Animal = Cat | Dog;

function assertNever(value: never): never {
  throw new Error(`Unhandled animal: ${value}`);
}

function makeSound(animal: Animal): void {
  if (animal instanceof Cat) {
    animal.meow();
  } else if (animal instanceof Dog) {
    animal.bark();
  } else {
    assertNever(animal);
  }
}

/** Example 3: 方向リテラル */
type Direction = "north" | "south" | "east" | "west";

function move(direction: Direction): void {
  if (direction === "north") return;
  if (direction === "south") return;
  if (direction === "east") return;
  if (direction === "west") return;
  assertNever(direction);
}
```
