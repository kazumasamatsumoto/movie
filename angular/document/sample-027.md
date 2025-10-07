# #027 「Component のドキュメント作成」

## 概要
Componentの使い方を文書化し、他の開発者が理解しやすくします。

## 学習目標
- JSDocの書き方を習得する
- Compodocの使い方を学ぶ
- 効果的なドキュメント作成方法を理解する

## 技術ポイント
- **JSDoc**: コード内ドキュメント
- **Compodoc**: 自動ドキュメント生成
- **README**: 使用方法の説明

## 📺 画面表示用コード（動画用）

```typescript
/**
 * ユーザー情報を表示するComponent
 * @example
 * <app-user [user]="userData" (selected)="onSelect($event)"></app-user>
 */
@Component({
  selector: 'app-user'
})
export class UserComponent {
  /** ユーザーデータ */
  @Input() user!: User;
  /** ユーザー選択時のイベント */
  @Output() selected = new EventEmitter<User>();
}
```

```bash
# Compodocでドキュメント生成
npm install -g @compodoc/compodoc
compodoc -p tsconfig.json -s
```

```markdown
# README.md
## UserComponent
ユーザー情報を表示

### Inputs
- user: User - 表示するユーザーデータ

### Outputs
- selected: EventEmitter<User> - 選択イベント
```

## ドキュメント項目

- Component概要
- Input/Output説明
- 使用例
- 注意事項

## 注意点

- 常に最新に保つ
- 具体的な例を含める
- わかりやすい言葉で

## 関連技術
- JSDoc
- Compodoc
- Technical Writing
- API Documentation
