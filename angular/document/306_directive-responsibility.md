# #306 「Directive の役割と責任」

## 概要
DirectiveはDOMの見た目や局所的な振る舞いに責任を持ち、ビジネスロジックや長期的な状態はサービスや他の層へ任せることで再利用性を高める。

## 学習目標
- Directiveに適した責任範囲を定義できるようになる
- ビューとロジックを分離する設計パターンを理解する
- テスト可能で保守しやすいDirective構造を構築する

## 技術ポイント
- HostBinding/Renderer2でビューの変更に限定
- サービス注入でビジネスルールを委譲
- @Input/@Outputでホストとの契約を明示

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appValidateState]', standalone: true })
export class ValidateStateDirective implements OnChanges {
  @Input({ alias: 'appValidateState', required: true }) state!: Signal<FormState>;
  constructor(private readonly alert: AlertService) {}
  ngOnChanges(): void {
    if (this.state().invalid) this.alert.notify('入力に不備があります');
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
export interface FormState {
  invalid: boolean;
  touched: boolean;
  errors: readonly string[];
}

@Injectable({ providedIn: 'root' })
export class AlertService {
  notify(message: string): void {
    // 実際はToastコンポーネントなどへ委譲
    console.warn('[alert]', message);
  }
}

@Directive({
  selector: '[appValidateState]',
  standalone: true
})
export class ValidateStateDirective implements OnChanges {
  @Input({ alias: 'appValidateState', required: true }) state!: Signal<FormState>;

  constructor(private readonly alert: AlertService) {}

  ngOnChanges(): void {
    const current = this.state();
    if (!current.touched) return;
    if (current.invalid) {
      this.alert.notify(current.errors.join('\n'));
    }
  }
}

@Component({
  selector: 'app-validate-state-demo',
  standalone: true,
  imports: [CommonModule, ValidateStateDirective],
  template: `
    <section [appValidateState]="state">
      <p>タッチ: {{ state().touched }}, 無効: {{ state().invalid }}</p>
    </section>
  `
})
export class ValidateStateDemoComponent {
  private readonly stateSignal = signal<FormState>({ invalid: true, touched: true, errors: ['必須項目です'] });
  protected state = computed(() => this.stateSignal());
}
```

## ベストプラクティス
- DirectiveはUI境界に集中させ、ビジネスルールはサービスやSignalsへ委譲する
- 副作用は`ngOnInit`や`ngOnDestroy`で開始・終了を管理し、ライフサイクルの整合性を保つ
- APIをInput/Outputに限定し、外部から想定外の依存を持ち込まない

## 注意点
- 大きな状態を内部で保持するとテストが困難になるため外部ストアに逃がす
- サービスに依存する場合はテスト用のスタブを用意し注入できる設計にする
- DOM操作が必要な場合でもRenderer2経由で行い、環境依存を避ける

## 関連技術
- Dependency Injection
- Angular Signals
- Smart/Dumbコンポーネントパターン
