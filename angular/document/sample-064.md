# #064 「ngOnInit - 初期化処理」

## 概要
コンポーネントが生成され、Inputの受け渡しが完了した後に呼び出される`ngOnInit`で初期化処理を実装する方法を学びます。

## 学習目標
- `ngOnInit`の呼び出しタイミングを説明できる
- 初期データ読み込みやSignal初期化を`ngOnInit`へ集約する
- コンストラクタとの役割分担を理解する

## 技術ポイント
- **OnInitインターフェース**: `ngOnInit(): void`を実装
- **初期化ロジック**: Input確定後に安全に実行できる
- **非同期処理**: `async/await`やObservableの購読で初回ロードを組み立てる

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
ngOnInit(): void {
  this.loadProfile();
}
```

```typescript
async loadProfile() {
  this.profile.set(await this.api.fetch());
}
```

```typescript
profile = signal<Profile | null>(null);
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, OnInit, signal } from '@angular/core';
import { CommonModule } from '@angular/common';

type Profile = { id: number; name: string; bio: string };

@Component({
  selector: 'app-profile-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './profile-card.component.html',
})
export class ProfileCardComponent implements OnInit {
  readonly profile = signal<Profile | null>(null);
  readonly loading = signal(true);

  async ngOnInit(): Promise<void> {
    this.loading.set(true);
    try {
      const data = await fakeFetchProfile();
      this.profile.set(data);
    } finally {
      this.loading.set(false);
    }
  }
}

async function fakeFetchProfile(): Promise<Profile> {
  await new Promise((resolve) => setTimeout(resolve, 300));
  return { id: 1, name: '四国めたん', bio: 'Angular講師 v20対応' };
}
```

```html
<section *ngIf="!loading(); else loadingTpl">
  <h2>{{ profile()?.name }}</h2>
  <p>{{ profile()?.bio }}</p>
</section>

<ng-template #loadingTpl>
  <p>読み込み中...</p>
</ng-template>
```

## ベストプラクティス
- 初期化は`ngOnInit`へまとめ、constructorは依存性注入と軽量な設定だけにする
- 非同期処理は`try/finally`でローディング状態を確実に切り替える
- フェッチ処理をサービスに分離し、テスト時はモックを注入できるようにする

## 注意点
- `ngOnInit`は一度だけ呼び出されるため、再表示時の再初期化には向かない（必要なら`ngOnChanges`などで補完）
- `await`を使うときは`ngOnInit`を`async`化し、例外処理を忘れない
- SSRでは初期化タイミングが異なるケースがあるため、プラットフォーム依存コードに注意する

## 関連技術
- Standalone ComponentとDI
- Signalsによるローディング状態管理
- Angular Routerの`resolve`ガードとの比較
