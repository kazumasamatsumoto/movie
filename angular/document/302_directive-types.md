# #302 「Directive の3つの種類」

## 概要
AngularのDirectiveはコンポーネント・構造・属性の3種類に分類され、UIを描画するか、DOM構造を制御するか、既存要素の振る舞いを調整するかで役割が異なる。

## 学習目標
- Directiveの主な種類と特徴を整理する
- プロジェクトでの配置・命名ルールを決める
- 適切な種類を選択する判断基準を身につける

## 技術ポイント
- Component Directiveはテンプレートを持つ
- Structural Directiveは`ViewContainerRef`/`TemplateRef`を扱う
- Attribute Directiveは`ElementRef`/`Renderer2`で見た目を調整する

```typescript
@Component({ selector: 'app-card', template: `<ng-content></ng-content>` })
export class CardComponent {}

@Directive({ selector: '[appShowIf]' })
export class ShowIfDirective { /* Structural */ }

@Directive({ selector: '[appAccent]' })
export class AccentDirective { /* Attribute */ }
```

## 💻 詳細実装例（学習用）
```typescript
export function classifyDirective(selector: string): 'component' | 'structural' | 'attribute' {
  if (!selector.includes('[') && !selector.includes('*') && !selector.startsWith('.')) return 'component';
  if (selector.startsWith('*')) return 'structural';
  return 'attribute';
}

console.log(classifyDirective('app-card')); // component
console.log(classifyDirective('*appIf'));   // structural
console.log(classifyDirective('[appAccent]')); // attribute
```

## ベストプラクティス
- 種類ごとにフォルダやプレフィックスを揃えて探索しやすくする
- Structural Directiveはテンプレート変換を伴うので責務を最小化する
- Attribute Directiveは直接DOM操作せずRenderer2を利用する

## 注意点
- コンポーネントを軽量なプレゼンテーション用途に使う場合でもテンプレートは必須
- Structural Directiveは単一要素にしか適用できないことを意識する
- 種類の違いを意識せず混在すると保守性が落ちる

## 関連技術
- `@Directive`
- `ViewContainerRef`
- Renderer2
