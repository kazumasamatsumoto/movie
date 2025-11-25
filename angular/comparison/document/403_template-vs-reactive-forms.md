# #403 「Template-driven Forms vs Reactive Forms あなたはどっち派？」

## 概要
テンプレート駆動フォームはHTML主導で迅速に作れる一方、Reactive FormsはTypeScriptで状態管理しやすくテストにも向く。フォーム規模や保守性に応じた選択が重要。

## 学習目標
- Template-drivenの構成と得意なシナリオを整理する
- Reactive Formsの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- Template-drivenを成り立たせる主要API/構成要素
- Reactive Formsで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**Template-driven：HTML中心で即実装**
```typescript
<form #heroForm="ngForm">
  <input name="name" [(ngModel)]="hero.name" required />
  <p *ngIf="heroForm.submitted && heroForm.invalid">名前は必須です</p>
</form>
```

**Reactive Forms：TypeScriptで制御**
```typescript
form = this.fb.nonNullable.group({
  name: ['', [Validators.required, Validators.minLength(3)]],
});

<form [formGroup]="form">
  <input formControlName="name" />
  <p *ngIf="form.get('name')?.invalid">invalid</p>
</form>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-hero-form',
  standalone: true,
  templateUrl: './hero-form.component.html',
})
export class HeroFormComponent {
  hero = { name: '' };

  readonly form = inject(FormBuilder).nonNullable.group({
    name: ['', [Validators.required, Validators.minLength(3)]],
  });

  saveTemplate(): void {
    console.log(this.hero);
  }

  saveReactive(): void {
    if (this.form.valid) {
      console.log(this.form.value);
    }
  }
}
```

## ベストプラクティス
- 小規模フォームはTemplate-drivenで素早く試作し、複雑になったらReactiveへ切り替える
- Reactive Formsでは`nonNullable`や型付きFormBuilderを使い型安全性を担保する
- 両方式を組み合わせる場合は責務を明確にし、同じフォームで二重バインドさせない

## 注意点
- Template-drivenは`ngModel`による二重バインディングが多いとパフォーマンスに影響する
- Reactive Formsは初期セットアップが冗長になりがちなのでFormBuilderユーティリティを活用する
- テンプレとReactiveのディレクティブを同じ要素に混在させるとエラーになる

## 関連技術
- FormsModule
- ReactiveFormsModule
- Typed Form Controls
