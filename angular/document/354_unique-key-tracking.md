# #354 「一意キーでの追跡」

## 概要
trackByで一意キーを返すことでアイテムの位置が変わってもDOMを再利用でき、リスト操作時のパフォーマンスが向上する。

## 学習目標
- 安定した一意キーの設計を理解する
- データソースと認証キーの連携を学ぶ
- trackBy適用時の挙動を把握する

## 技術ポイント
- 主キーやUUIDなど安定した識別子を使用
- 連番は再生成時に変わる可能性があるため適切ではない
- 一意キーがない場合はサーバーやストア層で付与を検討

## 📺 画面表示用コード（動画用）
```html
<li *ngFor="let note of notes; trackBy: trackByNoteId">
  {{ note.title }}
</li>
```

## 💻 詳細実装例（学習用）
```typescript
interface Note {
  noteId: string;
  title: string;
}

@Component({
  selector: 'app-unique-key-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ul>
      <li *ngFor="let note of notes; trackBy: trackByNoteId">{{ note.title }}</li>
    </ul>
  `
})
export class UniqueKeyDemoComponent {
  protected notes: Note[] = [
    { noteId: 'n-100', title: 'Structural Directive Overview' },
    { noteId: 'n-101', title: 'trackBy Deep Dive' }
  ];

  protected trackByNoteId(_: number, note: Note): string {
    return note.noteId;
  }
}
```

## ベストプラクティス
- バックエンドと協議して安定したキーを提供してもらう
- クライアント側で生成する場合も再生成しないようキャッシュする
- trackByとOnPushを組み合わせて不要なChange Detectionを避ける

## 注意点
- 一意キーが変わるとAngularが要素を別物と扱いDOMが再生成される
- キーの衝突が起きると描画が乱れるためテストで検出する
- 一意キーをJSONシリアライズすると型が変わる場合があるので慎重に扱う

## 関連技術
- Entity Adapter
- NGRX/Signal Store
- ChangeDetectionStrategy.OnPush
