# #066 「constructor vs ngOnInit の使い分け」

## 概要
Angularコンポーネントでconstructorと`ngOnInit`が担う役割の違いを整理し、依存性注入と初期化処理を分離する方法を学びます。

## 学習目標
- constructorが呼ばれるタイミングと責務を説明できる
- `ngOnInit`へ初期化処理を集約してテストしやすくする
- 依存性注入と初期ロジックの分離パターンを適用する

## 技術ポイント
- **constructor**: 依存性注入(DI)の受け取りと軽量な初期設定のみ
- **ngOnInit**: Input反映後の初期化フック、非同期処理に最適
- **テスト性向上**: constructorを軽量化するとモックDIやユニットテストが簡単

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
constructor(private readonly api: ProfileApi) {}
```

```typescript
ngOnInit(): void {
  this.loadProfile();
}
```

```typescript
private loadProfile() { /* 初期データ取得 */ }
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, OnInit, signal } from '@angular/core';

class ProfileApi {
  async fetch(): Promise<string> {
    await new Promise((r) => setTimeout(r, 200));
    return 'Angular Learner';
  }
}

@Component({
  selector: 'app-constructor-vs-init',
  standalone: true,
  templateUrl: './constructor-vs-init.component.html',
  providers: [ProfileApi],
})
export class ConstructorVsInitComponent implements OnInit {
  readonly name = signal('loading...');

  constructor(private readonly api: ProfileApi) {}

  ngOnInit(): void {
    void this.loadProfile();
  }

  private async loadProfile(): Promise<void> {
    this.name.set(await this.api.fetch());
  }
}
```

```html
<p>ユーザー名: {{ name() }}</p>
```

## ベストプラクティス
- constructorで状態を変えない。必要なプロパティ初期化はクラスフィールドに記述する
- 非同期処理は`ngOnInit`で実施し、`void`で呼び出して未処理Promise警告を防ぐ
- 依存するサービスやStoreはDIで受け取り、`ngOnInit`で利用開始する

## 注意点
- constructorでDOM操作やRouter遷移を行うとライフサイクルが崩れる
- `@Input`はconstructor時点では未設定なので利用しない
- DIの例外をキャッチしたい場合はconstructor内でtry/catchせず、`providers`設定を確認する

## 関連技術
- Standalone componentのDI
- Angular Testing Libraryでのコンポーネントテスト
- Signalsによる初期値設定
