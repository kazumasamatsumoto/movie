# #081 「Lifecycle での状態初期化」

## 概要
Lifecycle Hooksを活用してコンポーネント状態やフォーム値を初期化する際のパターンを学びます。

## 学習目標
- Input依存の状態初期化タイミングを理解する
- SignalやReactive Formを`ngOnInit`/`ngOnChanges`で整備する
- 初期化と再初期化を分離する

## 技術ポイント
- **ngOnInit**: Inputが揃った後の初期状態設定に最適
- **ngOnChanges**: 親からの変更に応じて再初期化する
- **Signals**: `signal`, `computed`で派生状態を生成

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@Input() profile?: UserProfile;
```

```typescript
ngOnInit() { this.setupState(); }
```

```typescript
ngOnChanges(c) { if (c['profile']) this.setupState(); }
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, Input, OnChanges, OnInit, SimpleChanges, computed, signal } from '@angular/core';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';

type UserProfile = { name: string; age: number };

@Component({
  selector: 'app-profile-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './profile-form.component.html',
})
export class ProfileFormComponent implements OnInit, OnChanges {
  @Input() profile: UserProfile | null = null;
  private readonly fb = inject(FormBuilder);
  readonly name = signal('');
  readonly age = signal(0);
  readonly summary = computed(() => `${this.name()} (${this.age()}歳)`);

  readonly form = this.fb.group({
    name: [''],
    age: [0],
  });

  ngOnInit(): void {
    this.syncFromProfile();
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['profile'] && !changes['profile'].firstChange) {
      this.syncFromProfile();
    }
  }

  private syncFromProfile(): void {
    if (!this.profile) {
      return;
    }
    this.name.set(this.profile.name);
    this.age.set(this.profile.age);
    this.form.setValue(this.profile);
  }
}
```

```html
<form [formGroup]="form">
  <label>名前 <input formControlName="name" /></label>
  <label>年齢 <input type="number" formControlName="age" /></label>
</form>
<p>プレビュー: {{ summary() }}</p>
```

## ベストプラクティス
- 初期化処理を専用メソッドにまとめ、`ngOnInit`と`ngOnChanges`から呼び出す
- Signalとフォームを併用し、フォーム値変更時にSignalへ反映するフローを構築する
- 初期化時に外部サービスへ依存する場合は非同期処理をawaitし、UI状態を更新する

## 注意点
- `form.setValue`はすべてのコントロールが必要。部分更新なら`patchValue`を使う
- 初期化メソッド内で`setValue`する際に`emitEvent: false`を指定して無限ループを防ぐことも検討
- 初期化が複数回走る可能性があるため、副作用を最小限に抑える

## 関連技術
- SignalsとReactive Formsの連携
- `input()`デコレータによるSignal化
- Angular Reactive Formsの初期値設定
