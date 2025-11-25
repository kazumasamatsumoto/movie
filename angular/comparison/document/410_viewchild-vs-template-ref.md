# #410 「ViewChild DOMアクセス vs template参照変数 あなたはどっち派？」

## 概要
ViewChildは強力だがライフサイクル管理が必要。template参照変数は簡潔だが参照先の型を自動で得られない。操作内容に応じて選ぶ。

## 学習目標
- ViewChildの構成と得意なシナリオを整理する
- template参照変数の採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- ViewChildを成り立たせる主要API/構成要素
- template参照変数で押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**ViewChild派：クラスから直接参照**
```typescript
@ViewChild('nameInput') input?: ElementRef<HTMLInputElement>;

focus() {
  this.input?.nativeElement.focus();
}
```

**template参照派：テンプレ内で完結**
```typescript
<input #nameInput />
<button (click)="focus(nameInput)">Focus</button>

focus(input: HTMLInputElement) {
  input.focus();
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-editor',
  standalone: true,
  templateUrl: './editor.component.html',
})
export class EditorComponent {
  @ViewChild('editor', { static: true })
  readonly editor?: ElementRef<HTMLTextAreaElement>;

  onTemplateFocus(input: HTMLInputElement) {
    input.focus();
  }
}
```

## ベストプラクティス
- DOM APIへ直接アクセスする必要がある場合のみViewChildを使い、普段はテンプレ変数で依存を明示する
- ViewChildで取得した要素は`Renderer2`経由で操作し、SSR互換を保つ
- テンプレ参照変数は引数で型注釈を付け、チーム内で共通命名を定める

## 注意点
- ViewChildは`ngAfterViewInit`前だとundefinedなのでアクセス時期を必ず確認する
- テンプレ参照変数は親子間で共有できないため必要以上に使うと渡し忘れが発生する
- テストでViewChild依存があるとモックが難しいため、`@ViewChild`の責務を小さくする

## 関連技術
- @ViewChild/@ViewChildren
- template reference variables
- Renderer2
