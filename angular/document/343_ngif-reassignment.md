# #343 「値の再代入と使用」

## 概要
`*ngIf`でエイリアスを受け取った値は読み取り専用で再代入できないため、テンプレートでは参照のみに留めコンポーネント側でロジックを扱う。

## 学習目標
- エイリアス値のライフサイクルとスコープを理解する
- 再代入の代わりにコンポーネントで状態を管理する方法を学ぶ
- テンプレートでの安全な値参照パターンを身につける

## 技術ポイント
- テンプレート内での再代入は不可、読み取りのみ
- コンポーネントでSignalやObservableを介して状態を更新
- エイリアスは型推論が効き、strictTemplatesで安全性が高まる

## 📺 画面表示用コード（動画用）
```html
<article *ngIf="user$ | async as user">
  <p>{{ user.name }}</p>
</article>
```

## 💻 詳細実装例（学習用）
```typescript
interface UserProfile {
  id: number;
  name: string;
}

@Component({
  selector: 'app-alias-usage-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div *ngIf="profile$ | async as profile; else loading">
      <h2>{{ profile.name }}</h2>
      <button type="button" (click)="rename(profile.id)">名前を変更</button>
    </div>
    <ng-template #loading>
      <p>読込中...</p>
    </ng-template>
  `
})
export class AliasUsageDemoComponent {
  private readonly subject = new BehaviorSubject<UserProfile>({ id: 1, name: '初期ユーザー' });
  protected profile$ = this.subject.asObservable();

  protected rename(id: number): void {
    this.subject.next({ id, name: '更新ユーザー' });
  }
}
```

## ベストプラクティス
- エイリアスは読み取り専用であることをコメントや命名で示す
- 値を更新したい場合はコンポーネントメソッドやSignalsで対応する
- テストでエイリアスが正しい値を参照しているか確認する

## 注意点
- テンプレート内で`profile = ...`のように代入するとビルドエラーになる
- エイリアスのスコープは`*ngIf`内に限定されるため外から参照できない
- `null`の場合に備えてelseテンプレートでフォールバックを提供する

## 関連技術
- BehaviorSubject
- Angular Signals
- Template Type Checking
