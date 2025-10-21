# #272 「DRY 原則の適用」

## 概要
DRY（Don't Repeat Yourself）原則は、繰り返し現れるロジックや表示を共通化し、変更を一箇所に集約することで保守性を高める指針である。

## 学習目標
- コンポーネント内外で重複を検出する方法を学ぶ
- Pipeやテンプレート共通化でDRYを実践する
- 過度な抽象化を避けつつバランスを取る

## 技術ポイント
- 共通テンプレートの抽出
- Standalone Pipeの活用
- 共通サービスによるユーティリティ提供

## 📺 画面表示用コード（動画用）
```typescript
@Pipe({ name: 'formatDate', standalone: true, pure: true })
export class FormatDatePipe implements PipeTransform {
  transform(value: string): string {
    return new Date(value).toLocaleDateString('ja-JP');
  }
}
```

```html
<ng-template #userRow let-user>
  <td>{{ user.name }}</td>
  <td>{{ user.joinedAt | formatDate }}</td>
</ng-template>
```

```typescript
@Component({ selector: 'app-user-table', standalone: true, imports: [FormatDatePipe], template: `<table><tr *ngFor="let user of users"><ng-container *ngTemplateOutlet="row; context: {$implicit: user}"></ng-container></tr></table><ng-template #row><td>{{ $implicit.name }}</td><td>{{ $implicit.joinedAt | formatDate }}</td></ng-template>` })
export class UserTableComponent {
  @Input({ required: true }) users: ReadonlyArray<UserVm> = [];
}
```

## 💻 詳細実装例（学習用）
```typescript
export function buildUserVm(partial: Partial<UserVm> = {}): UserVm {
  return {
    id: partial.id ?? crypto.randomUUID(),
    name: partial.name ?? '未設定',
    joinedAt: partial.joinedAt ?? new Date().toISOString(),
  };
}
```

## ベストプラクティス
- 重複が発生した時点でPipeやTemplateとして抽出する
- 共通化後はテストを追加し意図しない変更を検知する
- DRY適用箇所をドキュメント化して再利用先を明確にする

## 注意点
- 抽象化のメリットがない場合は無理に共通化しない
- Templateを共有する場合はContextを明確に定義する
- Pipe内で重たい処理を行わない

## 関連技術
- Standalone Pipe
- TemplateRef
- Test Data Builder
