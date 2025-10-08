# #237 「動的フォーム生成」

## 概要
フォーム定義をデータ（JSONなど）から読み込み、動的にフォームコンポーネントを生成する手法をまとめます。フィールドごとのコンポーネントを動的に挿入し、Reactive Formsと連携します。

## 学習目標
- フィールド定義に基づいてコンポーネントを動的生成する手順を理解する
- 各フィールドコンポーネントにFormControlを渡し、値を集約する方法を習得する
- Factory/Resolverパターンを使ってフィールド種類を拡張する

## 技術ポイント
- **フィールド定義**: `[{ type: 'text', label: '名前', controlName: 'name' }, ...]`
- **ComponentMap**: フィールドタイプをコンポーネントにマッピング
- **FormGroup連携**: `formGroup.get(controlName)`を動的コンポーネントへ渡す

## 📺 画面表示用コード（動画用）

```typescript
const ref = this.host.createComponent(fieldMap[field.type]);
ref.instance.control = this.form.get(field.controlName);
```

```typescript
ref.instance.config = field;
```

```typescript
this.form.valueChanges.subscribe(console.log);
```

## 💻 詳細実装例（学習用）
```typescript
// dynamic-form.component.ts
import { Component, ComponentRef, Input, ViewChild, ViewContainerRef } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { TextFieldComponent } from './fields/text-field.component';
import { SelectFieldComponent } from './fields/select-field.component';
import { FieldConfig } from './field-config';

const FIELD_COMPONENTS = {
  text: TextFieldComponent,
  select: SelectFieldComponent,
} as const;

@Component({
  selector: 'app-dynamic-form',
  standalone: true,
  imports: [TextFieldComponent, SelectFieldComponent],
  templateUrl: './dynamic-form.component.html',
})
export class DynamicFormComponent {
  @Input({ required: true }) form!: FormGroup;
  @Input() fields: FieldConfig[] = [];

  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  refs: ComponentRef<any>[] = [];

  ngOnChanges(): void {
    if (!this.form || !this.host) return;
    this.host.clear();
    this.refs.forEach((ref) => ref.destroy());
    this.refs = [];
    for (const field of this.fields) {
      const component = FIELD_COMPONENTS[field.type];
      if (!component) continue;
      const ref = this.host.createComponent(component);
      ref.instance.config = field;
      ref.instance.control = this.form.get(field.controlName);
      this.refs.push(ref);
    }
  }
}
```

```html
<!-- dynamic-form.component.html -->
<form [formGroup]="form">
  <ng-container #host></ng-container>
</form>
```

## ベストプラクティス
- フィールド定義を型付けし、コンポーネントが受け取るConfigを明確にする
- 未知のフィールドタイプはログを出すなど、デバッグしやすくする
- 再描画が多い場合は`trackBy`や差分更新を導入し、不要なdestroy/createを避ける

## 注意点
- フォームコントロールが存在しない場合はエラーを防ぐためフォールバックを用意する
- コンポーネントマップを動的に拡張できるよう、プラグインパターンを採用するケースもある
- 大規模フォームではパフォーマンスを測定し、遅延ロードや仮想化を検討する

## 関連技術
- 動的Componentのイベント・入力（#226, #227）
- プラグインアーキテクチャ（#240）
- Angular Reactive Forms API
