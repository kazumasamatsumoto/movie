# #404 「*ngIf/*ngFor vs v20 Control Flow あなたはどっち派？」

## 概要
従来の`*`構文は安定性と互換性が高い一方、新しいControl Flow構文は読みやすさと診断メッセージが強力。段階的に導入してテンプレートの見通しを改善する。

## 学習目標
- 従来の構文の構成と得意なシナリオを整理する
- 新Control Flowの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- 従来の構文を成り立たせる主要API/構成要素
- 新Control Flowで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**従来：`*ngIf`と`*ngFor`のネスト**
```typescript
<ng-container *ngIf="heroes.length; else empty">
  <div *ngFor="let hero of heroes; trackBy: trackById">
    {{ hero.name }}
  </div>
</ng-container>
<ng-template #empty>登録なし</ng-template>
```

**新構文：`@if`/`@for`でシンプルに**
```typescript
@if (heroes().length) {
  @for (hero of heroes(); track hero.id) {
    <div>{{ hero.name }}</div>
  } @empty {
    <p>登録なし</p>
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-hero-board',
  standalone: true,
  templateUrl: './hero-board.component.html',
})
export class HeroBoardComponent {
  readonly heroes = signal<Hero[]>([]);

  trackById(_: number, hero: Hero) {
    return hero.id;
  }
}
```

## ベストプラクティス
- テンプレ差分を追いやすい箇所から`@if/@for`を導入してレビューコストを下げる
- カスタムディレクティブで`*`構文を使っている場合は段階的に互換APIを提供する
- `@for`の`track`句を必ず設定して差分レンダリングのパフォーマンスを確保する

## 注意点
- テンプレート内に`@`と`*`を混在させると可読性が落ちるので段階的に統一する
- ビルドターゲットがv17未満の場合は新構文が使えないためバージョンを確認する
- 国際化テンプレート生成など外部ツールが新構文に対応しているか事前に確認する

## 関連技術
- Angular Control Flow v17+
- `@if`/`@for`/`@switch`
- テンプレート最適化
