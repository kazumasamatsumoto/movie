# #401 「Signals vs RxJS あなたはどっち派？」

## 概要
Angular v20では状態管理にSignalsが加わり、従来のRxJSベース実装との選択基準が明確になった。コード量、学習コスト、イベント密度に応じて使い分けることで保守性とパフォーマンスを高められる。

## 学習目標
- RxJSの構成と得意なシナリオを整理する
- Signalsの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- RxJSを成り立たせる主要API/構成要素
- Signalsで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**RxJS派：push型イベントに強い**
```typescript
user$ = new BehaviorSubject<User>({ first: '', last: '' });
fullName$ = this.user$.pipe(map(u => `${u.first} ${u.last}`));

<input (input)="user$.next({ ...user$.value, first: $any($event.target).value })">
<p>{{ fullName$ | async }}</p>
```

**Signals派：購読解除と行数を削減**
```typescript
user = signal<User>({ first: '', last: '' });
fullName = computed(() => `${this.user().first} ${this.user().last}`);

<input (input)="user.update(u => ({ ...u, first: $any($event.target).value }))">
<p>{{ fullName() }}</p>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-profile-editor',
  standalone: true,
  templateUrl: './profile-editor.component.html'
})
export class ProfileEditorComponent {
  readonly profile = signal({ first: '', last: '' });
  readonly initials = computed(() =>
    this.profile().first.at(0)?.toUpperCase() + this.profile().last.at(0)?.toUpperCase()
  );

  private readonly profileSubject = new BehaviorSubject({ first: '', last: '' });
  readonly profile$ = this.profileSubject.asObservable();
  readonly initials$ = this.profile$.pipe(map(p => `${p.first.at(0) ?? ''}${p.last.at(0) ?? ''}`));

  updateFirst(value: string): void {
    this.profile.update(p => ({ ...p, first: value }));
    this.profileSubject.next({ ...this.profileSubject.value, first: value });
  }
}
```

## ベストプラクティス
- UIローカル状態や派生値はSignalsで簡潔に表現し、購読解除コストをゼロ化する
- WebSocketやドラッグ&ドロップなどイベント密度が高い箇所はRxJSで構成し、Signalへ橋渡しする
- A/B双方の実装をコードモッド可能に保ち、評価指標（行数、リークリスク、テスト容易性）を共有する

## 注意点
- Signalsはライブラリ連携が進行中のため、外部パッケージがRxJS前提なら無理に置換しない
- RxJSを残す場合も`takeUntilDestroyed`等で購読解除を徹底し、やらかしを防ぐ
- SignalInput/SignalOutputへ切り替える際は`ChangeDetectionStrategy.OnPush`でも動作を確認する

## 関連技術
- Angular Signals
- RxJS
- toSignal/toObservable
