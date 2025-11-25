#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


@dataclass(frozen=True)
class Entry:
    number: int
    slug: str
    title: str
    hook: str
    overview: str
    a_label: str
    a_prompt: str
    a_answer: str
    a_pain: str
    b_label: str
    b_answer: str
    b_usecase: str
    conclusion: str
    summary: str
    goals: list[str] | None
    tech_points: list[str] | None
    code_a_title: str
    code_a: str
    code_b_title: str
    code_b: str
    detail: str
    best_practices: list[str]
    cautions: list[str]
    related: list[str]


ENTRIES: list[Entry] = [
    Entry(
        number=401,
        slug="signals-vs-rxjs",
        title="Signals vs RxJS あなたはどっち派？",
        hook="状態管理ってSignalsとRxJS、みんな結局どっちを使ってるの？",
        overview="両方強力ですが、Angular v20でSignalsが公式プッシュされてから選択基準が変わりました。",
        a_label="RxJS",
        a_prompt="まずRxJS派のいいところを教えてよ。",
        a_answer="Subject/BehaviorSubjectで複数ストリームを合流できるので、状態と副作用を1本のパイプで制御できます。push型イベントは今でもRxが得意です。",
        a_pain="でもプロトタイプだとsubscribe解除を忘れてメモリリークしがちなんだよね…。",
        b_label="Signals",
        b_answer="そこがSignals派の強みです。`signal()`と`computed()`だけで派生状態を宣言し、テンプレートは`{{ fullName() }}`のように呼び出すだけ。購読解除や`AsyncPipe`を意識しません。",
        b_usecase="コード行数もRxJS実装だとサービス＋コンポーネントで40行、Signalsは20行で済んだよ。",
        conclusion="イベント駆動の複雑な同期ならRxJS、UIローカル状態や派生値ならSignals。あなたはどっち派が幸せかコメントで教えてください！",
        summary="Angular v20では状態管理にSignalsが加わり、従来のRxJSベース実装との選択基準が明確になった。コード量、学習コスト、イベント密度に応じて使い分けることで保守性とパフォーマンスを高められる。",
        goals=None,
        tech_points=None,
        code_a_title="RxJS派：push型イベントに強い",
        code_a=dedent(
            """\
            user$ = new BehaviorSubject<User>({ first: '', last: '' });
            fullName$ = this.user$.pipe(map(u => `${u.first} ${u.last}`));

            <input (input)="user$.next({ ...user$.value, first: $any($event.target).value })">
            <p>{{ fullName$ | async }}</p>
            """
        ),
        code_b_title="Signals派：購読解除と行数を削減",
        code_b=dedent(
            """\
            user = signal<User>({ first: '', last: '' });
            fullName = computed(() => `${this.user().first} ${this.user().last}`);

            <input (input)="user.update(u => ({ ...u, first: $any($event.target).value }))">
            <p>{{ fullName() }}</p>
            """
        ),
        detail=dedent(
            """\
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
            """
        ),
        best_practices=[
            "UIローカル状態や派生値はSignalsで簡潔に表現し、購読解除コストをゼロ化する",
            "WebSocketやドラッグ&ドロップなどイベント密度が高い箇所はRxJSで構成し、Signalへ橋渡しする",
            "A/B双方の実装をコードモッド可能に保ち、評価指標（行数、リークリスク、テスト容易性）を共有する",
        ],
        cautions=[
            "Signalsはライブラリ連携が進行中のため、外部パッケージがRxJS前提なら無理に置換しない",
            "RxJSを残す場合も`takeUntilDestroyed`等で購読解除を徹底し、やらかしを防ぐ",
            "SignalInput/SignalOutputへ切り替える際は`ChangeDetectionStrategy.OnPush`でも動作を確認する",
        ],
        related=["Angular Signals", "RxJS", "toSignal/toObservable"],
    ),
    Entry(
        number=402,
        slug="standalone-vs-ngmodule",
        title="Standalone Components vs NgModule設計 あなたはどっち派？",
        hook="新規画面ってStandalone Componentで作る？それとも従来どおりNgModuleに束ねた方が安心かな？",
        overview="Angular v20は完全Standalone対応なので、設計思想次第でどちらも選べます。",
        a_label="NgModuleベース",
        a_prompt="まずNgModule派のメリットは？",
        a_answer="共有PipeやDirectiveを1か所で宣言・エクスポートでき、大規模プロジェクトで依存管理が明示的です。ライブラリもまだNgModule前提が多いですね。",
        a_pain="でもimports/exportsの書き忘れでビルドエラーになる事故は相変わらずだよ…。",
        b_label="Standalone",
        b_answer="Standaloneなら各Componentで`imports`を完結でき、`provideHttpClient`など機能ベースDIもローカル化できます。Lazy Routeも`loadComponent`だけで済みます。",
        b_usecase="CLIで`ng g component hero --standalone`すると依存がその場で閉じるのが気持ちいいね。",
        conclusion="共有部はModule、画面単位はStandaloneとハイブリッドにするのが移行も安全です。あなたはどっち派？",
        summary="Standalone ComponentとNgModuleベース構成は依存の明示度とスケーラビリティの考え方が違う。共有ライブラリの提供方法、DI構成、ルーティング記述の差を理解して適材適所で組み合わせる。",
        goals=None,
        tech_points=None,
        code_a_title="NgModule派：共有リソースを束ねる",
        code_a=dedent(
            """\
            @NgModule({
              declarations: [HeroListComponent],
              imports: [CommonModule, HeroesRoutingModule],
              exports: [HeroListComponent]
            })
            export class HeroesModule {}
            """
        ),
        code_b_title="Standalone派：コンポーネント内で完結",
        code_b=dedent(
            """\
            @Component({
              selector: 'app-hero-list',
              standalone: true,
              imports: [CommonModule, HeroCardComponent],
              templateUrl: './hero-list.component.html'
            })
            export class HeroListComponent {}
            """
        ),
        detail=dedent(
            """\
            // Standaloneブートストラップ
            bootstrapApplication(AppComponent, {
              providers: [
                provideRouter(routes),
                provideHttpClient(withFetch()),
              ],
            });

            // NgModuleブートストラップ
            @NgModule({
              declarations: [AppComponent],
              imports: [BrowserModule, HeroesModule],
              bootstrap: [AppComponent],
            })
            export class AppModule {}

            platformBrowserDynamic().bootstrapModule(AppModule);
            """
        ),
        best_practices=[
            "共有Pipe/DirectiveはModule化してまとめ、画面単位はStandaloneで小さく切る",
            "Standalone遷移時は`provideRouter`や`provideHttpClient`など機能ベースAPIを活用してDIを整理する",
            "ライブラリがNgModule依存の場合はFacade Moduleを残しつつ徐々にStandaloneへ移行する",
        ],
        cautions=[
            "StandaloneとNgModuleを混在させる際は同じ依存を二重登録しないように注意する",
            "Lazy RouteでStandaloneを使う場合も`canMatch`等のガード設定を忘れない",
            "Module前提のスキーマを利用するライブラリを無理にStandaloneに置き換えない",
        ],
        related=[
            "Standalone Component",
            "NgModule",
            "bootstrapApplication/provideRouter",
        ],
    ),
    Entry(
        number=403,
        slug="template-vs-reactive-forms",
        title="Template-driven Forms vs Reactive Forms あなたはどっち派？",
        hook="フォーム作るときって直感的なテンプレート駆動？それともReactive Formsでガッチリ組む？",
        overview="Angularは両方サポートしているので、チームのスピードとテスト容易性で選べます。",
        a_label="Template-driven",
        a_prompt="テンプレ派の良さから教えて！",
        a_answer="HTML中心で`[(ngModel)]`を書くだけなので、UIモックを素早く形にできます。ラピッドプロトタイプや小規模フォームに最適です。",
        a_pain="でもバリデーションをカスタムしたりテストを書くときにテンプレ側の状態追跡が大変なんだよね…。",
        b_label="Reactive Forms",
        b_answer="Reactive Formsは`FormGroup`/`FormControl`で状態をTypeScript側に集約するので、値変化の購読や同期バリデーションがしやすいです。",
        b_usecase="FormBuilderで型を付けておくとテストも補完も楽だよ。",
        conclusion="小さく早くならTemplate、大型かつ型安全ならReactive。あなたのフォーム戦略はどっち派？",
        summary="テンプレート駆動フォームはHTML主導で迅速に作れる一方、Reactive FormsはTypeScriptで状態管理しやすくテストにも向く。フォーム規模や保守性に応じた選択が重要。",
        goals=None,
        tech_points=None,
        code_a_title="Template-driven：HTML中心で即実装",
        code_a=dedent(
            """\
            <form #heroForm="ngForm">
              <input name="name" [(ngModel)]="hero.name" required />
              <p *ngIf="heroForm.submitted && heroForm.invalid">名前は必須です</p>
            </form>
            """
        ),
        code_b_title="Reactive Forms：TypeScriptで制御",
        code_b=dedent(
            """\
            form = this.fb.nonNullable.group({
              name: ['', [Validators.required, Validators.minLength(3)]],
            });

            <form [formGroup]="form">
              <input formControlName="name" />
              <p *ngIf="form.get('name')?.invalid">invalid</p>
            </form>
            """
        ),
        detail=dedent(
            """\
            @Component({
              selector: 'app-hero-form',
              standalone: true,
              templateUrl: './hero-form.component.html',
            })
            export class HeroFormComponent {
              hero = { name: '' };

              readonly form = inject(FormBuilder).nonNullable.group({
                name: ['', [Validators.required, Validators.minLength(3)]],
              });

              saveTemplate(): void {
                console.log(this.hero);
              }

              saveReactive(): void {
                if (this.form.valid) {
                  console.log(this.form.value);
                }
              }
            }
            """
        ),
        best_practices=[
            "小規模フォームはTemplate-drivenで素早く試作し、複雑になったらReactiveへ切り替える",
            "Reactive Formsでは`nonNullable`や型付きFormBuilderを使い型安全性を担保する",
            "両方式を組み合わせる場合は責務を明確にし、同じフォームで二重バインドさせない",
        ],
        cautions=[
            "Template-drivenは`ngModel`による二重バインディングが多いとパフォーマンスに影響する",
            "Reactive Formsは初期セットアップが冗長になりがちなのでFormBuilderユーティリティを活用する",
            "テンプレとReactiveのディレクティブを同じ要素に混在させるとエラーになる",
        ],
        related=[
            "FormsModule",
            "ReactiveFormsModule",
            "Typed Form Controls",
        ],
    ),
    Entry(
        number=404,
        slug="ngif-vs-control-flow",
        title="*ngIf/*ngFor vs v20 Control Flow あなたはどっち派？",
        hook="テンプレートの条件分岐、まだ`*ngIf`と`*ngFor`をネストしてる？それともv20の`@if/@for`に乗り換えた？",
        overview="Angularの制御フローは共存期間なので、読みやすさ重視なら新構文が強いです。",
        a_label="従来の構文",
        a_prompt="旧構文を使い続ける利点は？",
        a_answer="テンプレートが既存プロジェクトと互換で、ライブラリ断片も`*`構文前提なので移行コストが低いです。",
        a_pain="でも`<ng-container>`だらけでネストが深くなってレビューがつらいんだよね…。",
        b_label="新Control Flow",
        b_answer="`@if`/`@for`は波括弧の中にロジックを閉じ込められ、`@switch`もTypeScriptに近い書き味です。`track`句や`empty`句も標準になりました。",
        b_usecase="`@for (hero of heroes(); track hero.id)`って書けるの、読みやすくて感動するよ。",
        conclusion="互換性が必要な画面は従来構文のままでもOK。新規は`@if/@for`でテンプレの圧縮を体験してみて！",
        summary="従来の`*`構文は安定性と互換性が高い一方、新しいControl Flow構文は読みやすさと診断メッセージが強力。段階的に導入してテンプレートの見通しを改善する。",
        goals=None,
        tech_points=None,
        code_a_title="従来：`*ngIf`と`*ngFor`のネスト",
        code_a=dedent(
            """\
            <ng-container *ngIf="heroes.length; else empty">
              <div *ngFor="let hero of heroes; trackBy: trackById">
                {{ hero.name }}
              </div>
            </ng-container>
            <ng-template #empty>登録なし</ng-template>
            """
        ),
        code_b_title="新構文：`@if`/`@for`でシンプルに",
        code_b=dedent(
            """\
            @if (heroes().length) {
              @for (hero of heroes(); track hero.id) {
                <div>{{ hero.name }}</div>
              } @empty {
                <p>登録なし</p>
              }
            }
            """
        ),
        detail=dedent(
            """\
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
            """
        ),
        best_practices=[
            "テンプレ差分を追いやすい箇所から`@if/@for`を導入してレビューコストを下げる",
            "カスタムディレクティブで`*`構文を使っている場合は段階的に互換APIを提供する",
            "`@for`の`track`句を必ず設定して差分レンダリングのパフォーマンスを確保する",
        ],
        cautions=[
            "テンプレート内に`@`と`*`を混在させると可読性が落ちるので段階的に統一する",
            "ビルドターゲットがv17未満の場合は新構文が使えないためバージョンを確認する",
            "国際化テンプレート生成など外部ツールが新構文に対応しているか事前に確認する",
        ],
        related=[
            "Angular Control Flow v17+",
            "`@if`/`@for`/`@switch`",
            "テンプレート最適化",
        ],
    ),
    Entry(
        number=405,
        slug="eventemitter-vs-signaloutput",
        title="@Output EventEmitter vs SignalOutput あなたはどっち派？",
        hook="@OutputってまだEventEmitter派？SignalOutputに切り替えるメリットって大きいかな？",
        overview="Angular v17+はSignalベース出力が入り、親子通信の書き味が変わりました。",
        a_label="EventEmitter",
        a_prompt="まずEventEmitter派の強みは？",
        a_answer="従来のAPIでチーム全員が慣れており、`emit()`で同期/非同期を制御できます。既存ライブラリとも互換です。",
        a_pain="でも`EventEmitter`は実態がSubjectなので、unsubscribe忘れや`emit`の型安全性が気になるんだよね…。",
        b_label="SignalOutput",
        b_answer="`SignalOutput`は`result = output<number>();`のように宣言し、`result.emit(値)`でシグナルとして伝播します。Signalsと同じリアクティブグラフに乗るのでテストが楽です。",
        b_usecase="親側も`(result)`ではなく`result` Signalを購読するだけで状態合成できるのが嬉しい！",
        conclusion="互換が必要な箇所はEventEmitter、Signalベースでまとめたい画面はSignalOutput。あなたはどっち派？",
        summary="EventEmitterは成熟しているが手動購読や型安全性に課題がある。SignalOutputは宣言的にイベントを表現し、Signalsグラフへ統合できるため新規アプリに向く。",
        goals=None,
        tech_points=None,
        code_a_title="EventEmitter派：従来の親子通信",
        code_a=dedent(
            """\
            @Output() result = new EventEmitter<number>();

            calc() {
              this.result.emit(this.value * 2);
            }

            <child (result)="onResult($event)" />
            """
        ),
        code_b_title="SignalOutput派：signal()グラフに統合",
        code_b=dedent(
            """\
            result = output<number>();

            calc() {
              this.result.emit(this.value() * 2);
            }

            <child (result)="resultSignal.set($event)" />
            """
        ),
        detail=dedent(
            """\
            @Component({
              selector: 'app-child',
              standalone: true,
              template: `<button (click)="notify()">Send</button>`,
            })
            export class ChildComponent {
              readonly count = signal(0);
              readonly result = output<number>();

              notify(): void {
                this.count.update(v => v + 1);
                this.result.emit(this.count());
              }
            }
            """
        ),
        best_practices=[
            "幅広い互換性が必要な共有コンポーネントはEventEmitterを維持し、アプリ固有部分からSignalOutputを導入する",
            "SignalOutputを使う際は親側もSignalベースで受け取り、`effect`や`computed`に組み込む",
            "EventEmitterでも`takeUntilDestroyed`を使って購読解除をシステム化する",
        ],
        cautions=[
            "SignalOutputはAngular v17+限定なのでバージョン条件を満たしているか確認する",
            "SignalとRxJSの境界で同一イベントを二重に処理しないように整理する",
            "EventEmitterの`async`フラグなど独自機能はSignalOutputに存在しないため挙動差を把握する",
        ],
        related=[
            "EventEmitter",
            "SignalOutput API",
            "Angular Signals",
        ],
    ),
    Entry(
        number=406,
        slug="input-vs-signalinput",
        title="@Input setter vs SignalInput あなたはどっち派？",
        hook="親からの入力、まだ`@Input() set value(...)`で処理してる？SignalInputに置き換えると何が嬉しい？",
        overview="SignalInputは`signal()`と同じAPIで入力状態を扱えるようになり、変更検知がシンプルになります。",
        a_label="@Input setter",
        a_prompt="setter派の良いところは？",
        a_answer="入力を受け取った瞬間にバリデーションや変換を行えるので、`ngOnChanges`なしでも柔軟です。古いAngularとの互換性も高いです。",
        a_pain="でもsetter内で副作用を書きすぎるとテストしづらいし、`SimpleChanges`を自前で追いかけるのは骨が折れる…。",
        b_label="SignalInput",
        b_answer="`value = input.required<number>();`のように宣言し、`this.value()`で常に最新値を参照できます。`computed`で派生状態を作れるのでsetterにビジネスロジックを書かなくて済みます。",
        b_usecase="`SignalInput`を使うと`ngOnChanges`レスで差分が扱えるのは気持ちいいね。",
        conclusion="互換性優先ならsetter、Signalで統一したいならSignalInput。コメントでどっち派か教えて！",
        summary="@Input setterは柔軟だが副作用を抱え込みやすい。SignalInputは入力値をSignal化し、派生状態やSignalOutputと合わせてスッキリ書ける。",
        goals=None,
        tech_points=None,
        code_a_title="setter派：入力で副作用を実行",
        code_a=dedent(
            """\
            private _userId = '';

            @Input()
            set userId(value: string) {
              this._userId = value;
              this.fetchProfile();
            }
            """
        ),
        code_b_title="SignalInput派：Signalとして受け取る",
        code_b=dedent(
            """\
            userId = input.required<string>();
            profile = computed(() => this.repo.load(this.userId()));

            refresh() {
              this.repo.refresh(this.userId());
            }
            """
        ),
        detail=dedent(
            """\
            @Component({
              selector: 'app-user-card',
              standalone: true,
              template: `
                <ng-container *ngIf="profile() as p">
                  <h3>{{ p.name }}</h3>
                </ng-container>
              `,
            })
            export class UserCardComponent {
              private readonly repo = inject(UserRepository);

              readonly userId = input.required<string>();
              readonly profile = toSignal(
                this.repo.profile$(this.userId()),
                { initialValue: null },
              );
            }
            """
        ),
        best_practices=[
            "SignalInputと`computed`を組み合わせて派生状態を作り、副作用は`effect`へ切り出す",
            "レガシーsetterは薄く保ち、SignalInputへ徐々に移行できるようFacadeを用意する",
            "入力が任意なら`input<string | undefined>`を使い、undefinedハンドリングを型で表現する",
        ],
        cautions=[
            "SignalInputはAngular v17+限定なのでバージョン互換を確認する",
            "setterとSignalInputを同じプロパティ名で併用しない",
            "SignalInputで受けた値を直接ミューテートしない（不変データを前提にする）",
        ],
        related=[
            "SignalInput API",
            "@Input setter",
            "toSignal/toObservable",
        ],
    ),
    Entry(
        number=407,
        slug="default-vs-onpush",
        title="ChangeDetection Default vs OnPush あなたはどっち派？",
        hook="ChangeDetection、デフォルト任せ？それとも迷わずOnPush派？",
        overview="検知戦略はパフォーマンスとDXのバランスがポイントです。",
        a_label="Default戦略",
        a_prompt="Default派の言い分は？",
        a_answer="Zone.jsが自動で検知を走らせてくれるので、`setTimeout`やDOMイベントを深く意識せずに開発できます。学習コストが低いです。",
        a_pain="でもコンポーネントが大量になると不要なチェックでCPUを使っちゃうんだよね…。",
        b_label="OnPush戦略",
        b_answer="`ChangeDetectionStrategy.OnPush`にするとInputsやイベント、Observable完了時のみ検知が走るので、無駄なレンダリングを抑えられます。Signalsとの相性も◎。",
        b_usecase="`OnPush`にしたらfpsグラフが安定したよ。",
        conclusion="プロトタイプはDefault、本番はOnPush＋ルールで運用。あなたのチームはどっち派？",
        summary="ChangeDetection Defaultは使いやすいが余計な検知が増える。OnPushは管理コストが上がる代わりにパフォーマンスが安定するため、チームの運用力に合わせて選ぶ。",
        goals=None,
        tech_points=None,
        code_a_title="Default：宣言不要で自動検知",
        code_a=dedent(
            """\
            @Component({
              selector: 'app-dashboard',
              templateUrl: './dashboard.component.html',
            })
            export class DashboardComponent {
              counter = 0;

              incrementLater() {
                setTimeout(() => this.counter++, 1000);
              }
            }
            """
        ),
        code_b_title="OnPush：必要なタイミングだけ検知",
        code_b=dedent(
            """\
            @Component({
              selector: 'app-dashboard',
              changeDetection: ChangeDetectionStrategy.OnPush,
              templateUrl: './dashboard.component.html',
            })
            export class DashboardComponent {
              readonly counter = signal(0);

              incrementLater() {
                setTimeout(() => this.counter.update(v => v + 1), 1000);
              }
            }
            """
        ),
        detail=dedent(
            """\
            @Component({
              selector: 'app-score-card',
              changeDetection: ChangeDetectionStrategy.OnPush,
              template: `
                <h4>{{ score() }}</h4>
                <button (click)="increase()">+1</button>
              `,
            })
            export class ScoreCardComponent {
              readonly score = signal(0);

              increase(): void {
                this.score.update((v) => v + 1);
              }
            }
            """
        ),
        best_practices=[
            "Default戦略は検証用や小規模画面に限定し、主要画面はOnPushで統一する",
            "OnPush採用時は不変データとSignalsをセットで使い、`markForCheck`乱用を避ける",
            "プロジェクトルールとしてどこにどの戦略を使うかドキュメント化する",
        ],
        cautions=[
            "OnPushでMutableオブジェクトを渡すと更新に気づかないので必ずコピーする",
            "Default戦略はゾーン外の非同期処理で変化が伝わらないケースがある",
            "ChangeDetectionの混在はバグ源になるのでルールなしに混ぜない",
        ],
        related=[
            "ChangeDetectionStrategy",
            "Signalベース更新",
            "markForCheck/detectChanges",
        ],
    ),
    Entry(
        number=408,
        slug="zone-vs-zoneless",
        title="Zone.js依存 vs Zoneless構成 あなたはどっち派？",
        hook="Zone.jsを切り離してZonelessにする勇気ある？それともZoneのオート検知に甘える？",
        overview="Angular v17では`provideExperimentalZonelessChangeDetection`が登場し、Signals主体ならZonelessでも開発できるようになりました。",
        a_label="Zone.jsあり",
        a_prompt="Zone.jsを残す利点は？",
        a_answer="既存コードや外部ライブラリがZoneを前提にしているので互換性を気にしなくて済みます。change detectionも自動です。",
        a_pain="でもZoneがあるとデバッグ時のスタックが深いし、SSRやWeb Workerで余計なコストが発生するんだよね…。",
        b_label="Zoneless",
        b_answer="`provideExperimentalZonelessChangeDetection()`を有効にし、Signalsや`rxEffects`で明示的に更新すれば、自分でレンダリングタイミングを制御できます。パフォーマンスが読みやすくなります。",
        b_usecase="ZonelessにしたらDevToolsのプロファイルがすっきりして原因追跡が捗ったよ。",
        conclusion="互換が必要ならZone継続、Signals全面採用ならZonelessに挑戦。あなたはどっち派？",
        summary="Zone.jsは互換性とDXを担保するが、ZonelessはSignals＋明示的更新でパフォーマンスと理解を得られる。アプリの成熟度に合わせて選ぶ。",
        goals=None,
        tech_points=None,
        code_a_title="Zone.jsあり：既定の`bootstrapApplication`",
        code_a=dedent(
            """\
            bootstrapApplication(AppComponent, {
              providers: [
                provideRouter(routes),
              ],
            });
            """
        ),
        code_b_title="Zoneless：実験的プロバイダを適用",
        code_b=dedent(
            """\
            bootstrapApplication(AppComponent, {
              providers: [
                provideExperimentalZonelessChangeDetection(),
                provideRouter(routes),
              ],
            });
            """
        ),
        detail=dedent(
            """\
            import { provideExperimentalZonelessChangeDetection } from '@angular/core';

            bootstrapApplication(AppComponent, {
              providers: [
                provideExperimentalZonelessChangeDetection(),
                provideRouter(routes),
              ],
            });
            """
        ),
        best_practices=[
            "Zoneless化する場合はSignalsや`effect`でUI更新を記述し、`runOutsideAngular`に頼らない",
            "外部ライブラリがZone依存の場合はAdapter層を設け、完全移行まではZoneを残す",
            "Zoneあり構成でも`bootstrapApplication`で必要なプロバイダだけを読み込んでコストを抑える",
        ],
        cautions=[
            "Zonelessはまだexperimental扱いなのでサポート範囲を把握しておく",
            "Zoneを外すと`setTimeout`等で自動検知されないためSignals以外の更新をどう扱うか決める",
            "SSRやHydrationを使う場合はZonelessとの組み合わせを事前検証する",
        ],
        related=[
            "Zone.js",
            "provideExperimentalZonelessChangeDetection",
            "Signals/effect",
        ],
    ),
    Entry(
        number=409,
        slug="ngoninit-vs-resolver",
        title="ngOnInit API呼び出し vs Route Resolver あなたはどっち派？",
        hook="一覧データ、コンポーネントの`ngOnInit`で取得する？それともルートResolverで先に用意する？",
        overview="データロードの場所でUXが変わるので、要件に合わせた設計が必要です。",
        a_label="ngOnInit fetch",
        a_prompt="ngOnInit派のメリットは？",
        a_answer="実装がシンプルで、画面固有のロジックをコンポーネント内に閉じ込められます。API呼び出しの順序も柔軟です。",
        a_pain="でも画面表示後にローディングインジケータが見えてしまい、ルータ遷移中にデータがないとチラつくんだよね…。",
        b_label="Route Resolver",
        b_answer="Resolverならルート遷移前にデータを取得し、遷移が完了した瞬間にコンポーネントへ渡せます。フェイル時もルータで制御可能です。",
        b_usecase="Resolverでリダイレクト条件をまとめたら、ガード実装がスリム化したよ。",
        conclusion="UX重視ならResolver、柔軟性重視ならngOnInit。あなたはどっち派？",
        summary="コンポーネント内でAPIを呼ぶと実装が楽だが表示が遅れる。一方Resolverはルート遷移と統合されUXは良いが、再利用には工夫が必要。",
        goals=None,
        tech_points=None,
        code_a_title="ngOnInit派：コンポーネント内で取得",
        code_a=dedent(
            """\
            ngOnInit(): void {
              this.repo.list().subscribe((items) => {
                this.items = items;
              });
            }
            """
        ),
        code_b_title="Resolver派：ルートで事前取得",
        code_b=dedent(
            """\
            export const routes: Routes = [
              {
                path: 'heroes',
                loadComponent: () => import('./heroes.component'),
                resolve: { heroes: heroesResolver },
              },
            ];
            """
        ),
        detail=dedent(
            """\
            export const heroesResolver: ResolveFn<Hero[]> = () => {
              const repo = inject(HeroRepository);
              return repo.list();
            };

            @Component({
              selector: 'app-heroes',
              standalone: true,
              template: `
                <ng-container *ngIf="heroes$ | async as heroes">
                  <app-hero-card *ngFor="let hero of heroes" [hero]="hero" />
                </ng-container>
              `,
            })
            export class HeroesComponent {
              readonly heroes$ = inject(ActivatedRoute).data.pipe(map(data => data['heroes'] as Hero[]));
            }
            """
        ),
        best_practices=[
            "API呼び出しが軽い一覧はResolverで先読みし、重い処理はコンポーネント内に分割する",
            "Resolverはpure functionとして定義し、DIでサービスを注入してテストしやすくする",
            "ngOnInit派でも`takeUntilDestroyed`で購読解除を忘れない",
        ],
        cautions=[
            "Resolverで失敗した場合の遷移制御（リトライ・リダイレクト）を必ず設計する",
            "Resolverに元々重い複数APIを詰め込むと初回遷移が遅くなる",
            "ngOnInitで取得する場合はSkeleton UIなどでUX低下を補う",
        ],
        related=[
            "Route Resolver",
            "ActivatedRoute.data",
            "ngOnInitとRxJS",
        ],
    ),
    Entry(
        number=410,
        slug="viewchild-vs-template-ref",
        title="ViewChild DOMアクセス vs template参照変数 あなたはどっち派？",
        hook="DOM操作したいとき、`@ViewChild`でがっつり参照？それとも`#ref`のテンプレ変数で軽く済ませる？",
        overview="参照方法によってライフサイクルやテストの書き方が変わります。",
        a_label="ViewChild",
        a_prompt="ViewChild派の良さを教えて！",
        a_answer="コンポーネント/ディレクティブのインスタンスに直接アクセスでき、`ngAfterViewInit`で安全に操作できます。DIも効きます。",
        a_pain="でもテストダブルを差し替えないと密結合になりがちだし、`{ static: true }`の指定を忘れるとundefinedなんだよね…。",
        b_label="template参照変数",
        b_answer="テンプレ内で`#inputRef`のように宣言し、メソッドに`inputRef.value`を渡せば依存が明確でテストもしやすいです。`ViewChild`を減らせます。",
        b_usecase="`<input #name (blur)='save(name.value)' />`って書くと依存が透き通るのが好き。",
        conclusion="高度な操作はViewChild、ライトな参照はtemplate変数。あなたの推しは？",
        summary="ViewChildは強力だがライフサイクル管理が必要。template参照変数は簡潔だが参照先の型を自動で得られない。操作内容に応じて選ぶ。",
        goals=None,
        tech_points=None,
        code_a_title="ViewChild派：クラスから直接参照",
        code_a=dedent(
            """\
            @ViewChild('nameInput') input?: ElementRef<HTMLInputElement>;

            focus() {
              this.input?.nativeElement.focus();
            }
            """
        ),
        code_b_title="template参照派：テンプレ内で完結",
        code_b=dedent(
            """\
            <input #nameInput />
            <button (click)="focus(nameInput)">Focus</button>

            focus(input: HTMLInputElement) {
              input.focus();
            }
            """
        ),
        detail=dedent(
            """\
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
            """
        ),
        best_practices=[
            "DOM APIへ直接アクセスする必要がある場合のみViewChildを使い、普段はテンプレ変数で依存を明示する",
            "ViewChildで取得した要素は`Renderer2`経由で操作し、SSR互換を保つ",
            "テンプレ参照変数は引数で型注釈を付け、チーム内で共通命名を定める",
        ],
        cautions=[
            "ViewChildは`ngAfterViewInit`前だとundefinedなのでアクセス時期を必ず確認する",
            "テンプレ参照変数は親子間で共有できないため必要以上に使うと渡し忘れが発生する",
            "テストでViewChild依存があるとモックが難しいため、`@ViewChild`の責務を小さくする",
        ],
        related=[
            "@ViewChild/@ViewChildren",
            "template reference variables",
            "Renderer2",
        ],
    ),
    Entry(
        number=411,
        slug="constructor-vs-inject",
        title="constructor注入 vs inject()関数 あなたはどっち派？",
        hook="サービス注入ってconstructor派？それとも関数`inject()`で書くのが好み？",
        overview="Angular v14で`inject()`が登場し、DIの書き味が分岐しました。",
        a_label="constructor注入",
        a_prompt="constructor派のメリットは？",
        a_answer="依存がクラスのシグネチャで明示され、テストダブルの差し替えが直感的。長年のスタンダードです。",
        a_pain="でもStandalone関数や`provideEffects`内で使えないし、フィールドを追加するたびにconstructorが伸びる…。",
        b_label="inject()関数",
        b_answer="`const router = inject(Router);`のようにトップレベルで呼び出せるので、Standalone関数や`signal`初期化でもDIが使えます。ツリーシェイキングも有利です。",
        b_usecase="`readonly repo = inject(RepoService);`と書くとプロパティ宣言で完結するのが気持ちいい！",
        conclusion="クラス中心ならconstructor、Signal中心ならinject。あなたはどっち派？",
        summary="constructor注入は明示的で既存コードとの互換が高い。inject()はStandalone APIと相性がよく、関数領域でもDIが使える。",
        goals=None,
        tech_points=None,
        code_a_title="constructor派：依存を引数で宣言",
        code_a=dedent(
            """\
            constructor(private readonly router: Router) {}

            goDetail(id: string) {
              this.router.navigate(['/heroes', id]);
            }
            """
        ),
        code_b_title="inject派：フィールドで完結",
        code_b=dedent(
            """\
            private readonly router = inject(Router);

            goDetail(id: string) {
              this.router.navigate(['/heroes', id]);
            }
            """
        ),
        detail=dedent(
            """\
            export const heroResolver: ResolveFn<Hero> = () => {
              const repo = inject(HeroRepository);
              const route = inject(ActivatedRouteSnapshot);
              return repo.find(route.params['id']);
            };
            """
        ),
        best_practices=[
            "クラスの依存はconstructorで宣言し、内部ユーティリティやSignals初期化は`inject()`を併用する",
            "`inject()`呼び出しはトップレベルで行い、メソッド内で毎回呼ばない",
            "DIを単体テストする際はTestBedの`overrideProvider`で共通化する",
        ],
        cautions=[
            "`inject()`は同期的に呼ぶ必要があり、非同期関数内では使えない",
            "constructor注入でも`public`で露出させると意図せずAPIになるため`private`/`protected`を付ける",
            "同じ依存をconstructorとinject両方で取得しない",
        ],
        related=[
            "Angular Dependency Injection",
            "inject() API",
            "Standalone関数",
        ],
    ),
    Entry(
        number=412,
        slug="httpclientmodule-vs-providehttpclient",
        title="HttpClientModule vs provideHttpClient あなたはどっち派？",
        hook="HTTP設定、まだ`HttpClientModule`をNgModuleでインポート？`provideHttpClient`で機能別に組み立ててる？",
        overview="v15以降はStandalone向けに`provideHttpClient`が登場し、設定方法が2通りになりました。",
        a_label="HttpClientModule",
        a_prompt="HttpClientModule派のメリットは？",
        a_answer="NgModuleに1回importするだけでアプリ全体にHTTPが提供され、既存ドキュメントも豊富です。レガシー構成と親和性が高いです。",
        a_pain="でも`HttpClientModule`を複数Moduleでimportすると重複しやすいし、オプションの組み合わせを注入するのが手間で…。",
        b_label="provideHttpClient",
        b_answer="`bootstrapApplication`で`provideHttpClient(withFetch(), withInterceptors([...]))`のように機能をチェーンでき、必要な場所だけで設定できます。",
        b_usecase="SSRだけ`withFetch()`、ブラウザだけ`withXsrfConfiguration()`みたいに分けられるの最高！",
        conclusion="NgModule構成ならHttpClientModule、新規StandaloneならprovideHttpClient。あなたはどっち派？",
        summary="HttpClientModuleは古典的だが簡単。provideHttpClientは機能ベースでツリーシェイカブルな設定ができ、Standalone構成にフィットする。",
        goals=None,
        tech_points=None,
        code_a_title="HttpClientModule派：NgModuleにimport",
        code_a=dedent(
            """\
            @NgModule({
              imports: [BrowserModule, HttpClientModule],
              bootstrap: [AppComponent],
            })
            export class AppModule {}
            """
        ),
        code_b_title="provideHttpClient派：機能を組み合わせる",
        code_b=dedent(
            """\
            bootstrapApplication(AppComponent, {
              providers: [
                provideHttpClient(
                  withFetch(),
                  withInterceptors([authInterceptor]),
                ),
              ],
            });
            """
        ),
        detail=dedent(
            """\
            export function authInterceptor(req: HttpRequest<unknown>, next: HttpHandlerFn) {
              return next(req.clone({ setHeaders: { Authorization: 'Bearer token' } }));
            }
            """
        ),
        best_practices=[
            "NgModule運用時でも`HttpClientModule`をrootだけでimportし、子Moduleからは再度importしない",
            "`provideHttpClient`では関数オプションを分離してテストしやすいように保つ",
            "SSRやHydrationが必要な場合は`withFetch()`を利用し、環境別プロバイダで切り替える",
        ],
        cautions=[
            "HttpClientModuleとprovideHttpClientを同時に登録すると二重DIになる可能性がある",
            "interceptorを`multi: true`で提供する場合、順序を把握して副作用を避ける",
            "`provideHttpClient`のオプションは関数呼び出し順に適用されるので意図どおり並べる",
        ],
        related=[
            "HttpClientModule",
            "provideHttpClient",
            "HTTP Interceptors",
        ],
    ),
    Entry(
        number=413,
        slug="material-vs-tailwind",
        title="Angular Material vs Tailwind CSS あなたはどっち派？",
        hook="UIスタイル、Materialコンポーネントで固める？Tailwindで自由に組む？",
        overview="Angular公式はMaterial 3を提供しつつ、ユーティリティ系CSSも人気。デザイン要件で選びたいところです。",
        a_label="Angular Material",
        a_prompt="Material派の推しポイントは？",
        a_answer="アクセシブルなUIコンポーネントが揃い、テーマとダークモード切り替えも標準です。FormFieldやDialogなど動作保証付き。",
        a_pain="でもカスタマイズが深くなるとcss変数だらけで重くなるし、独自デザインだと逆にブレーキになる…。",
        b_label="Tailwind CSS",
        b_answer="ユーティリティクラスでデザイン自由度が高く、ファイルサイズも抑えやすい。Angular CLIにも公式サポートが入りました。",
        b_usecase="MaterialのDialogは使いつつ、レイアウトはTailwindってハイブリッドが最高かもね。",
        conclusion="規約重視ならMaterial、スピード重視ならTailwind。あなたはどっち派？",
        summary="Angular Materialは品質保証済みUIセットで素早く統一感を出せる。Tailwindはデザイン自由度とビルド時の最適化が強い。併用も視野に入れる。",
        goals=None,
        tech_points=None,
        code_a_title="Material派：完成度の高いUIキット",
        code_a=dedent(
            """\
            @Component({
              selector: 'app-login',
              standalone: true,
              imports: [MatButtonModule, MatFormFieldModule, MatInputModule],
              template: `
                <mat-form-field>
                  <mat-label>Email</mat-label>
                  <input matInput />
                </mat-form-field>
                <button mat-raised-button color="primary">Login</button>
              `,
            })
            export class LoginComponent {}
            """
        ),
        code_b_title="Tailwind派：ユーティリティで柔軟に",
        code_b=dedent(
            """\
            <form class="space-y-3">
              <label class="block text-sm font-medium text-slate-500">Email</label>
              <input class="w-full rounded border px-3 py-2 focus:ring-2 focus:ring-emerald-500" />
              <button class="w-full rounded bg-emerald-500 py-2 font-semibold text-white">Login</button>
            </form>
            """
        ),
        detail=dedent(
            """\
            // tailwind.config.cjs
            module.exports = {
              content: ['./src/**/*.{html,ts}'],
              theme: { extend: {} },
              plugins: [],
            };
            """
        ),
        best_practices=[
            "Materialはデータ入力やアクセシビリティ要件が厳しい画面で採用し、テーマをFigmaと連携して管理する",
            "Tailwindはデザイントークンを`tailwind.config`にまとめ、クラス乱立を防ぐ",
            "二者併用時はCSS変数・フォント設定を共通レイヤーに置き、重複を避ける",
        ],
        cautions=[
            "Materialコンポーネントはバンドルサイズが大きくなるので`standalone`インポートで必要分だけ使う",
            "Tailwindはクラス名が長くなりがちなので`@apply`や部品化ルールを決める",
            "Design Systemの方針が揺れると両者のメンテが二重になるため意思決定を明確にする",
        ],
        related=[
            "Angular Material 3",
            "Tailwind CSS",
            "Design System",
        ],
    ),
    Entry(
        number=414,
        slug="ngrx-vs-signals-store",
        title="NgRx Store vs Signals Store あなたはどっち派？",
        hook="グローバル状態、まだNgRx StoreでActions/Reducer書いてる？Signal Storeで宣言的にしてる？",
        overview="NgRx 17はSignals Storeを提供し、Action/ReducerスタイルとSignalスタイルを選べるようになりました。",
        a_label="NgRx Store",
        a_prompt="NgRx Store派の強みは？",
        a_answer="Action/Reducer/Effectで状態遷移が明示され、DevToolsでタイムトラベルも可能。大規模チームでベストプラクティスが確立しています。",
        a_pain="でもActionやReducerのボイラープレートが多く、少人数チームだとパターンを覚えるだけで一苦労…。",
        b_label="Signals Store",
        b_answer="`signalStore`で`withState`, `withMethods`, `withComputed`を組み合わせるだけで、SignalsグラフとしてStoreを構築できます。Action定義は不要です。",
        b_usecase="`effect`内でHTTPを叩いても型の補完が効くのが気持ちいい！",
        conclusion="ガバナンス重視なら従来NgRx、スピード重視ならSignal Store。あなたはどっち派？",
        summary="NgRx Storeは厳格なアーキテクチャで大規模向き。Signals Storeはボイラープレートを減らし、Signalと親和性の高い状態管理を提供する。",
        goals=None,
        tech_points=None,
        code_a_title="NgRx Store派：ReducerとActionで管理",
        code_a=dedent(
            """\
            export const heroReducer = createReducer(
              initialState,
              on(loadHeroesSuccess, (state, { heroes }) => ({ ...state, heroes }))
            );
            """
        ),
        code_b_title="Signals Store派：宣言的に状態定義",
        code_b=dedent(
            """\
            export const HeroesStore = signalStore(
              withState(initialState),
              withMethods((store, repo = inject(HeroRepository)) => ({
                load: () => repo.list().subscribe(heroes => store.patchState({ heroes })),
              })),
            );
            """
        ),
        detail=dedent(
            """\
            @Injectable({ providedIn: 'root' })
            export class HeroesSignalsStore extends signalStore(
              withState({ heroes: [] as Hero[] }),
              withComputed(store => ({
                count: computed(() => store.heroes().length),
              })),
              withMethods((store, repo = inject(HeroRepository)) => ({
                load: () => repo.list().subscribe(heroes => store.patchState({ heroes })),
              })),
            ) {}
            """
        ),
        best_practices=[
            "NgRx StoreはAction命名やFeature構成をガイドライン化して統一する",
            "Signal Storeは`withHooks`で初期ロードなどを記述し、副作用を`effect`へ逃がす",
            "両方を併用する場合はドメイン境界を決め、Signal StoreをFeature Storeのfacadeにする",
        ],
        cautions=[
            "Signal StoreはNgRx v16+が必要で、DevToolsとの統合が限定的",
            "NgRx StoreのActionを乱立させると可読性が落ちるので命名規約を徹底する",
            "Signals StoreでObservableを直接購読する際はメモリリーク対策を忘れない",
        ],
        related=[
            "@ngrx/store",
            "@ngrx/signals",
            "signalStore API",
        ],
    ),
    Entry(
        number=415,
        slug="componentstore-vs-signal-service",
        title="NgRx ComponentStore vs Signalサービス あなたはどっち派？",
        hook="ローカル状態、ComponentStoreでEffect組む？それともサービスにSignal置いて済ませる？",
        overview="Feature単位の状態管理はComponentStoreとSignalサービスの二択が人気です。",
        a_label="ComponentStore",
        a_prompt="ComponentStore派の良さは？",
        a_answer="`updater`と`effect`で状態遷移をパターン化でき、RxJSの力を借りて非同期を制御できます。テストもしやすいです。",
        a_pain="でも`setState/patchState`などAPIが多くて、Signalsに寄せ始めると重複感が…。",
        b_label="Signalサービス",
        b_answer="シンプルに`readonly filters = signal<Filters>({...})`などをサービスへ置き、`computed`で派生値を提供します。依存が少なくて済みます。",
        b_usecase="Signalサービス＋`toObservable`で必要な場所だけRxJSに渡すハイブリッドが軽い！",
        conclusion="複雑なストリームはComponentStore、UIローカルならSignalサービス。あなたはどっち派？",
        summary="ComponentStoreはRxJSベースで複雑なEffectに強い。Signalサービスは軽量で読みやすい。Feature規模とメンバーの習熟で選ぶ。",
        goals=None,
        tech_points=None,
        code_a_title="ComponentStore派：updater/effectで制御",
        code_a=dedent(
            """\
            export class FiltersStore extends ComponentStore<FiltersState> {
              readonly updateStatus = this.updater((state, status: string) => ({
                ...state,
                status,
              }));
            }
            """
        ),
        code_b_title="Signalサービス派：signal()で保持",
        code_b=dedent(
            """\
            @Injectable({ providedIn: 'root' })
            export class FiltersService {
              readonly status = signal<'all' | 'done'>('all');
              readonly computedLabel = computed(() => `status: ${this.status()}`);
            }
            """
        ),
        detail=dedent(
            """\
            export class TodosStore extends ComponentStore<TodosState> {
              readonly load = this.effect((trigger$) =>
                trigger$.pipe(
                  switchMap(() => this.repo.list()),
                  tapResponse(
                    (todos) => this.patchState({ todos }),
                    (error) => this.patchState({ error }),
                  ),
                ),
              );
            }
            """
        ),
        best_practices=[
            "ComponentStoreはFeature単位に閉じ込め、責務を増やしすぎない",
            "Signalサービスは`computed`で派生値を公開し、直接状態を書き換えられないよう`update`メソッドを設ける",
            "両方式の共通インターフェースを定義し、テストダブルを入れ替えられるようにする",
        ],
        cautions=[
            "ComponentStoreのEffectは購読解除が必要なので`takeUntilDestroyed`を使う",
            "SignalサービスでもMutableオブジェクトをそのまま更新すると検知されないので不変更新する",
            "どちらもUIから直接RxJS/Signal APIを触らせずFacadeを通す",
        ],
        related=[
            "@ngrx/component-store",
            "Angular Signals",
            "Facadeパターン",
        ],
    ),
    Entry(
        number=416,
        slug="csr-vs-ssr",
        title="CSRオンリー vs SSR+Hydration あなたはどっち派？",
        hook="Angularアプリ、CSRだけで押し切る？SSR+Hydrationまでやり切る？",
        overview="パフォーマンスとSEO要件でレンダリング戦略が大きく変わります。",
        a_label="CSRオンリー",
        a_prompt="CSR派のメリットは？",
        a_answer="デプロイトポがシンプルで、ホスティングも静的CDNだけで済みます。開発者体験も軽いです。",
        a_pain="でも初回真っ白問題やSEOクローラへの露出が弱く、離脱率が気になる…。",
        b_label="SSR+Hydration",
        b_answer="`provideServerRendering`やHydration機能を使えば、初回HTMLをサーバで生成しクライアントで再利用できます。LCPやSEOが改善します。",
        b_usecase="SSR化したらCore Web Vitalsが一気にグリーンになった！",
        conclusion="要件次第で使い分け。あなたの案件はCSR派？SSR派？",
        summary="CSRは構成がシンプルでコストを抑えられる。SSR+Hydrationは実装コストがかかるがUXとSEOが向上する。",
        goals=None,
        tech_points=None,
        code_a_title="CSR派：静的ホスティングに配置",
        code_a=dedent(
            """\
            ng build --configuration production
            npx http-server dist/app
            """
        ),
        code_b_title="SSR派：server.tsを用意",
        code_b=dedent(
            """\
            export function app(): Promise<Express> {
              const server = express();
              server.use(express.static(join(process.cwd(), 'dist/app/browser')));
              server.get('*', ngExpressEngine);
              return server;
            }
            """
        ),
        detail=dedent(
            """\
            bootstrapApplication(AppComponent, {
              providers: [
                provideClientHydration(),
              ],
            });
            """
        ),
        best_practices=[
            "CSR構成でも`ngx-build-plus`や`esbuild`でバンドルサイズを管理し、初回表示を最適化する",
            "SSR導入時はAPIレスポンス時間も測定し、`TransferState`でデータ再取得を防ぐ",
            "Hydration対象のコンポーネントは副作用を`ngOnInit`以降に寄せて一致させる",
        ],
        cautions=[
            "SSRはNode.jsランタイムが必要で、デプロイ先のコストが上がる",
            "ブラウザAPIを`ngOnInit`前に使うとSSRでクラッシュする",
            "CSRからSSRへ移行する際は環境判定コードを必ずテストする",
        ],
        related=[
            "Angular SSR",
            "Hydration",
            "TransferState",
        ],
    ),
    Entry(
        number=417,
        slug="hydration-vs-prerender",
        title="Hydration vs Prerenderオンリー あなたはどっち派？",
        hook="SSRした後、Hydrationまで行う？それともPrerenderで静的吐き出しだけにする？",
        overview="SSR導入後も、クライアント側の振る舞い方で2パターンがあります。",
        a_label="Prerenderオンリー",
        a_prompt="Prerenderだけにする利点は？",
        a_answer="静的HTMLを生成してCDN配信でき、Nodeサーバが不要。公開後は完全な静的サイトとして扱えます。",
        a_pain="でも動的インタラクションが必要なページでは結局CSRと同じ課題が残るんだよね…。",
        b_label="Hydration",
        b_answer="`provideClientHydration()`を設定すれば、SSRで描画したDOMをクライアントが引き継ぎ、イベントバインドを再利用できます。JSの再レンダリングを減らせます。",
        b_usecase="Hydration有効化で上書きレンダリングが消え、パフォーマンス計測が安定した！",
        conclusion="静的サイトならPrerender、SPA挙動が欲しいならHydration。コメントでどっち派か教えて！",
        summary="Prerenderは配信コストを抑えられSEOも満たせるが、クライアントJSは別で走る。HydrationはSSR DOMを再利用し、初回のJS処理を削減する。",
        goals=None,
        tech_points=None,
        code_a_title="Prerender：`ng prerender`で静的出力",
        code_a=dedent(
            """\
            ng build && ng run app:prerender
            // dist/app/browserに静的HTMLが展開
            """
        ),
        code_b_title="Hydration：クライアントで再利用",
        code_b=dedent(
            """\
            bootstrapApplication(AppComponent, {
              providers: [
                provideClientHydration(),
              ],
            });
            """
        ),
        detail=dedent(
            """\
            import { provideClientHydration } from '@angular/platform-browser';

            bootstrapApplication(AppComponent, {
              providers: [provideClientHydration()],
            });
            """
        ),
        best_practices=[
            "Prerender対象は更新頻度の低いページに限定し、ISR（Incremental Static Regeneration）的なフローを整える",
            "Hydrationするページは副作用を`afterRender`等に逃し、サーバとクライアントのDOM差分を無くす",
            "動的・静的ページを混在させる場合はルーティングで明示的に分離する",
        ],
        cautions=[
            "Prerenderは大量ページでビルド時間が伸びるため監視が必要",
            "HydrationしないとクライアントJSが再描画するため一瞬チラつくことがある",
            "Hydration済みページに直接DOM操作を入れるとミスマッチになるので避ける",
        ],
        related=[
            "Angular prerender",
            "Client Hydration",
            "Server-side rendering",
        ],
    ),
    Entry(
        number=418,
        slug="routermodule-vs-providerouter",
        title="RouterModule vs provideRouter あなたはどっち派？",
        hook="ルーティング設定、まだ`RouterModule.forRoot`？`provideRouter`に移行した？",
        overview="Standalone時代は`provideRouter`が推奨され、設定ファイルも関数化できます。",
        a_label="RouterModule",
        a_prompt="RouterModule派のメリットは？",
        a_answer="従来のNgModuleと親和性が高く、`forRoot/forChild`パターンが確立しているので既存プロジェクトで安心です。",
        a_pain="でもModuleを量産するとimportsがネストし、`loadChildren`の書き方も複雑に…。",
        b_label="provideRouter",
        b_answer="`bootstrapApplication`で`provideRouter(routes)`を渡すだけで完結し、`withComponentInputBinding`など機能オプションがチェーンできます。",
        b_usecase="Functional GuardやResolverと組み合わせると`routes.ts`だけで全て完結するのが最高！",
        conclusion="Module構成ならRouterModule、新規StandaloneならprovideRouter。あなたはどっち派？",
        summary="RouterModuleはNgModuleベースの習熟を活かせる。provideRouterはStandaloneアプリのルーティングをシンプルに記述でき、付加機能も選べる。",
        goals=None,
        tech_points=None,
        code_a_title="RouterModule派：NgModuleで宣言",
        code_a=dedent(
            """\
            @NgModule({
              imports: [RouterModule.forRoot(routes)],
              exports: [RouterModule],
            })
            export class AppRoutingModule {}
            """
        ),
        code_b_title="provideRouter派：関数で提供",
        code_b=dedent(
            """\
            const routes: Routes = [...];

            bootstrapApplication(AppComponent, {
              providers: [
                provideRouter(routes, withComponentInputBinding()),
              ],
            });
            """
        ),
        detail=dedent(
            """\
            export const routes: Routes = [
              {
                path: 'heroes',
                loadComponent: () => import('./heroes/hero-page.component').then(m => m.HeroPageComponent),
              },
            ];
            """
        ),
        best_practices=[
            "RouterModule運用時もルート設定は単一ファイルにまとめ、Lazy Load境界を明示する",
            "provideRouterを使う際は`withViewTransitions`, `withPreloading`など機能オプションを積極的に活用する",
            "両アプローチが混在する場合は`RouterModule.forChild`の中身もStandalone Componentにするなど徐々に移行する",
        ],
        cautions=[
            "RouterModuleとprovideRouterを同時に提供しない、二重DIになる可能性がある",
            "Functional Guardなどv15以降のAPIを使う際はバージョンを確認",
            "ルート定義ファイルは循環参照が起きやすいのでimportパスを管理する",
        ],
        related=[
            "RouterModule.forRoot",
            "provideRouter",
            "withComponentInputBinding",
        ],
    ),
    Entry(
        number=419,
        slug="class-guard-vs-functional",
        title="クラスベースGuard vs 関数型Guard あなたはどっち派？",
        hook="ルートのGuard、`CanActivate`クラスで書く？それとも関数型に切り替えた？",
        overview="Angular v15で関数型ガードが追加され、DIの柔軟性が上がりました。",
        a_label="クラスベース",
        a_prompt="クラスガード派の良さは？",
        a_answer="`CanActivate`などのインターフェースを実装するだけでDIが使え、テストもモッククラスを差し替えればOK。長年のスタンダードです。",
        a_pain="でもファイルが嵩むし、Routeごとの細かな条件を書くとStatefulになりがち…。",
        b_label="関数型Guard",
        b_answer="`const canActivateHero: CanActivateFn = () => { ... }`のように関数ベースで書け、`inject()`でサービスを参照できます。Route定義と同じファイルで完結させやすいです。",
        b_usecase="ResolverやGuardを同じ`routes.ts`にまとめられるの気持ちいい！",
        conclusion="共有ガードはクラス、局所的なロジックは関数と使い分けたい。あなたはどっち派？",
        summary="クラスガードは再利用性とテスト容易性が高い。関数型はStandalone時代にマッチし、DIも自由。ルート特性に応じて選択する。",
        goals=None,
        tech_points=None,
        code_a_title="クラス派：`CanActivate`を実装",
        code_a=dedent(
            """\
            @Injectable({ providedIn: 'root' })
            export class AuthGuard implements CanActivate {
              constructor(private readonly auth: AuthService, private readonly router: Router) {}
              canActivate(): boolean {
                return this.auth.isSignedIn() || this.router.createUrlTree(['/login']);
              }
            }
            """
        ),
        code_b_title="関数派：`CanActivateFn`で完結",
        code_b=dedent(
            """\
            export const authGuard: CanActivateFn = () => {
              const auth = inject(AuthService);
              const router = inject(Router);
              return auth.isSignedIn() || router.createUrlTree(['/login']);
            };
            """
        ),
        detail=dedent(
            """\
            export const routes: Routes = [
              {
                path: 'admin',
                loadComponent: () => import('./admin.component'),
                canActivate: [authGuard],
              },
            ];
            """
        ),
        best_practices=[
            "よく使うガードはクラスとして切り出し、局所的な条件は関数で`routes.ts`に書く",
            "`inject()`で取り出す依存はトップレベルに保持し、副作用を避ける",
            "ガードの戻り値に`UrlTree`を活用し、リダイレクト先を明示する",
        ],
        cautions=[
            "関数型ガードは`inject()`を同期的にしか呼べないので注意",
            "クラスガードと関数ガードが混在する場合、命名規約を決めて可読性を保つ",
            "ガードで重いAPI呼び出しをすると遷移体験が悪化するためResolverやPreloadingへ逃がす",
        ],
        related=[
            "CanActivate/CanMatch",
            "Functional Guards",
            "inject() API",
        ],
    ),
    Entry(
        number=420,
        slug="nopreload-vs-preloadall",
        title="NoPreloading vs PreloadAllModules あなたはどっち派？",
        hook="Lazy Loadモジュール、読み込み戦略はNoPreloading？それとも全部先読み？",
        overview="Angular Routerは標準で二つのプリロード戦略を提供し、UXとデータ通信のバランスを取れます。",
        a_label="NoPreloading",
        a_prompt="先読みしない派のメリットは？",
        a_answer="初回トラフィックが最小になり、不要なバンドルをダウンロードしません。モバイル回線で有利です。",
        a_pain="でも2画面目に遷移した瞬間にダウンロードが走って待ち時間が発生…。",
        b_label="PreloadAllModules",
        b_answer="アイドル時間を使って全Lazyモジュールを読み込み、次の遷移を即時にします。規模が有限なら一度読み込むだけです。",
        b_usecase="Dashboard→設定画面の遷移が体感ゼロになってユーザー満足度が上がったよ。",
        conclusion="通信量を抑えるか遷移速度を優先するか。あなたはどっち派？",
        summary="NoPreloadingは通信量と初回負荷を抑える。PreloadAllModulesは後続遷移の体感速度を上げる。ハイブリッドも可能。",
        goals=None,
        tech_points=None,
        code_a_title="NoPreloading：標準設定",
        code_a=dedent(
            """\
            provideRouter(routes);
            """
        ),
        code_b_title="PreloadAllModules：全て先読み",
        code_b=dedent(
            """\
            provideRouter(routes, withPreloading(PreloadAllModules));
            """
        ),
        detail=dedent(
            """\
            provideRouter(routes, withPreloading(PreloadAllModules));
            """
        ),
        best_practices=[
            "トラフィックに余裕がある管理画面などはPreloadAllModulesでUXを最適化する",
            "大規模アプリはカスタムPreloadingStrategyを実装し、優先度の高いルートだけ先読みする",
            "ネットワーク状況に応じて戦略を切り替えたい場合は`NetworkInformation` API等と連携する",
        ],
        cautions=[
            "PreloadAllModulesは大量のLazyモジュールがあると帯域を圧迫する",
            "NoPreloadingはユーザーが初めて訪れる画面で待ち時間が必ず発生する",
            "戦略変更後はCore Web Vitalsを計測し、効果を確認する",
        ],
        related=[
            "Angular Router PreloadingStrategy",
            "withPreloading",
            "PreloadAllModules",
        ],
    ),
    Entry(
        number=421,
        slug="trackby-vs-none",
        title="ngFor trackBy無し vs trackBy導入 あなたはどっち派？",
        hook="リスト描画、`trackBy`書いてる？省略してる？",
        overview="リスト更新頻度と要素の複雑さで`trackBy`の有無がパフォーマンスに直結します。",
        a_label="trackByなし",
        a_prompt="trackByを省略する利点は？",
        a_answer="コードが短くて済み、プロトタイプでサクッと表示するには十分。Angularがindexをkeyにして再描画します。",
        a_pain="でも配列が更新されるたびにDOMが全部作り直されて、アニメーションやフォーカスが消える…。",
        b_label="trackByあり",
        b_answer="`trackBy`で一意キーを返せば、DOMノードを再利用できて再描画コストが激減します。Signalsとも相性◎。",
        b_usecase="`trackById`書いただけでCPUプロファイルが緑になったよ！",
        conclusion="小規模なら省略も可、でも本番はtrackBy推奨。あなたはどっち派？",
        summary="trackByなしは楽だが差分レンダリングができずパフォーマンスが劣る。trackByは少しのコードでUXが向上する。",
        goals=None,
        tech_points=None,
        code_a_title="trackByなし：そのままループ",
        code_a=dedent(
            """\
            <li *ngFor="let hero of heroes">{{ hero.name }}</li>
            """
        ),
        code_b_title="trackByあり：キーで追跡",
        code_b=dedent(
            """\
            <li *ngFor="let hero of heroes; trackBy: trackById">
              {{ hero.name }}
            </li>

            trackById(_: number, hero: Hero) {
              return hero.id;
            }
            """
        ),
        detail=dedent(
            """\
            @Component({
              selector: 'app-hero-list',
              standalone: true,
              templateUrl: './hero-list.component.html',
            })
            export class HeroListComponent {
              readonly heroes = signal<Hero[]>([]);

              trackById(_: number, hero: Hero) {
                return hero.id;
              }
            }
            """
        ),
        best_practices=[
            "IDがあるリストは必ずtrackByを定義し、Signals/Observablesの更新に備える",
            "配列の順序が頻繁に変わる場合はtrackByでもDOM再使用があるため、Keyの安定性を確認する",
            "コード生成ツールにもtrackByテンプレを組み込み、書き忘れを防ぐ",
        ],
        cautions=[
            "trackByが重い計算をすると逆にパフォーマンスを落とすため関数を軽量に保つ",
            "ユニークキーがない場合にindexを返すと効果がなくなる",
            "trackBy関数でオブジェクトを返すと参照が毎回変わり再描画が止まらない",
        ],
        related=[
            "*ngFor",
            "trackBy",
            "変更検知最適化",
        ],
    ),
    Entry(
        number=422,
        slug="img-vs-ngoptimizedimage",
        title="<img> vs NgOptimizedImage あなたはどっち派？",
        hook="画像の読み込み、素の`<img>`で済ませる？それとも`NgOptimizedImage`入れてる？",
        overview="Angular v15+は画像最適化ディレクティブを提供し、LCP改善が容易になりました。",
        a_label="素の<img>",
        a_prompt="プレーンimg派の強みは？",
        a_answer="HTML標準で書けて直感的。既存CMSからの出力をそのまま貼り付けられます。",
        a_pain="でも`width/height`忘れでCLSが発生したり、遅延読み込みを自前でやるのが手間…。",
        b_label="NgOptimizedImage",
        b_answer="`ngOptimizedImage`ディレクティブを付けるだけでプリロード最適化や`fetchpriority`が自動設定され、`fill`レイアウトなども使えます。",
        b_usecase="LCP画像に`priority`付けたらCore Web Vitalsが改善した！",
        conclusion="静的ページでも`NgOptimizedImage`はコスパ抜群。あなたはどっち派？",
        summary="素のimgは自由だが最適化を自分で管理する必要がある。NgOptimizedImageはAngularがレスポンシブ・遅延読み込み設定を肩代わりする。",
        goals=None,
        tech_points=None,
        code_a_title="素のimg：自己責任で最適化",
        code_a=dedent(
            """\
            <img src="/assets/hero.jpg" alt="hero" />
            """
        ),
        code_b_title="NgOptimizedImage：最適化込み",
        code_b=dedent(
            """\
            <img
              ngOptimizedImage
              [src]="hero.photo"
              width="320"
              height="200"
              priority
              alt="hero"
            />
            """
        ),
        detail=dedent(
            """\
            @Component({
              selector: 'app-hero-card',
              standalone: true,
              imports: [NgOptimizedImage],
              templateUrl: './hero-card.component.html',
            })
            export class HeroCardComponent {
              @Input() hero!: Hero;
            }
            """
        ),
        best_practices=[
            "LCP候補の画像は`priority`を付け、その他は`loading='lazy'`や`ngSrcset`でレスポンシブにする",
            "CMS等で画像URLを生成するなら`ngSrc`を使い、ビルド時検証を有効化する",
            "素のimgを使う場合も必ずwidth/heightを指定しCLSを避ける",
        ],
        cautions=[
            "NgOptimizedImageはAngular v15+が必要で、SSRとの組み合わせも検証する",
            "priorityを多用すると帯域を圧迫するので1ページ1〜2枚に制限する",
            "外部CDNのURLを使う際はCORS設定を確認する",
        ],
        related=[
            "NgOptimizedImage",
            "画像最適化",
            "Core Web Vitals",
        ],
    ),
    Entry(
        number=423,
        slug="css-vs-angular-animations",
        title="CSSトランジション vs Angular Animations あなたはどっち派？",
        hook="アニメーション、素のCSSでサクッと書く？Angular Animationsで状態管理までやる？",
        overview="シンプルなトランジションとリッチな状態遷移で使い分けたい領域です。",
        a_label="CSSトランジション",
        a_prompt="CSS派のメリットは？",
        a_answer="`transition`や`@keyframes`で手軽に実装でき、バンドルサイズ増加もほぼありません。デザイナーのハンドオフも楽です。",
        a_pain="でもコンポーネント状態と同期した複数ステップアニメーションは複雑になりがち…。",
        b_label="Angular Animations",
        b_answer="`trigger`, `state`, `transition`でコンポーネントの状態を直接制御でき、`AnimationBuilder`で動的生成も可能。Router Animationsもサポートします。",
        b_usecase="`@fade`トリガーを使うと状態変化とモーションを同じファイルで管理できてレビューが楽！",
        conclusion="軽量ならCSS、状態連動ならAngular Animations。あなたはどっち派？",
        summary="CSSトランジションは軽量で汎用的。Angular Animationsは状態管理や複雑なシーケンスに強い。要件に応じて選択する。",
        goals=None,
        tech_points=None,
        code_a_title="CSS派：クラスにtransitionを仕込む",
        code_a=dedent(
            """\
            .card {
              transition: transform 200ms ease;
            }
            .card:hover {
              transform: translateY(-4px);
            }
            """
        ),
        code_b_title="Angular Animations派：triggerで制御",
        code_b=dedent(
            """\
            @Component({
              animations: [
                trigger('fade', [
                  transition(':enter', [style({ opacity: 0 }), animate('200ms', style({ opacity: 1 }))]),
                  transition(':leave', [animate('200ms', style({ opacity: 0 }))]),
                ]),
              ],
            })
            """
        ),
        detail=dedent(
            """\
            @Component({
              selector: 'app-hero-card',
              standalone: true,
              animations: [
                trigger('highlight', [
                  state('active', style({ transform: 'scale(1.02)' })),
                  state('rest', style({ transform: 'scale(1)' })),
                  transition('rest <=> active', animate('150ms ease-in-out')),
                ]),
              ],
            })
            export class HeroCardComponent {
              state = signal<'rest' | 'active'>('rest');
            }
            """
        ),
        best_practices=[
            "CSSトランジションで済む箇所はCSSに寄せ、ロジックを薄く保つ",
            "Angular Animationsを使う場合はトリガー名/状態名の命名を統一し、Router Animationsとも整合させる",
            "パフォーマンス計測でアニメーションがメインスレッドを圧迫していないか確認する",
        ],
        cautions=[
            "Angular Animationsはランタイムサイズが増えるため必要な箇所だけに絞る",
            "CSSアニメーションでも`will-change`指定の乱用は避ける",
            "SSR環境でアニメーションを使用する場合は`BrowserAnimationsModule`導入を忘れない",
        ],
        related=[
            "Angular Animations",
            "CSS transition/keyframes",
            "BrowserAnimationsModule",
        ],
    ),
    Entry(
        number=424,
        slug="karma-vs-jest",
        title="Karma/Jasmine vs Jest/Vitest あなたはどっち派？",
        hook="ユニットテスト、CLI標準のKarma/Jasmineを使い続ける？JestやVitestへ切り替える？",
        overview="Angular v17のビルド刷新でJest/Vitestが公式ドキュメントにも載り、選択肢が広がりました。",
        a_label="Karma/Jasmine",
        a_prompt="Karma派の強みは？",
        a_answer="Angular CLIが標準サポートしており、ブラウザ実行なのでDOM互換が完全です。レガシープロジェクトで互換性が高いです。",
        a_pain="でもブラウザ立ち上げコストが高く、ウォッチモードが遅い…。",
        b_label="Jest/Vitest",
        b_answer="Node上で実行され、スナップショットや高速ウォッチが魅力。`ng test --watch=false`でESBuild経由の実行も可能です。",
        b_usecase="Vitest移行でテスト時間が半分になったよ！",
        conclusion="ブラウザ互換重視ならKarma、速度重視ならJest/Vitest。あなたはどっち派？",
        summary="Karma/Jasmineは公式標準でDOM互換が強み。Jest/VitestはモダンなDXと速度が高い。プロダクトの特性に合わせる。",
        goals=None,
        tech_points=None,
        code_a_title="Karma派：angular.jsonで標準設定",
        code_a=dedent(
            """\
            "test": {
              "builder": "@angular-devkit/build-angular:karma",
              "options": {
                "polyfills": ["zone.js/testing"]
              }
            }
            """
        ),
        code_b_title="Jest/Vitest派：builderを切り替え",
        code_b=dedent(
            """\
            "test": {
              "builder": "@angular-devkit/build-angular:jest",
              "options": {
                "setupFile": "src/setup-jest.ts"
              }
            }
            """
        ),
        detail=dedent(
            """\
            // vitest.config.ts
            export default defineConfig({
              test: {
                globals: true,
                environment: 'jsdom',
              },
            });
            """
        ),
        best_practices=[
            "既存Karmaでも`esbuild`ベースのbuilderへ切り替え、ウォッチ体験を改善する",
            "Jest/Vitest導入時は`setup`ファイルで`zone.js/testing`互換を整備する",
            "テストランナーを混在させる場合はCIジョブを分割し、実行時間を計測する",
        ],
        cautions=[
            "Jest/Vitestでは一部のブラウザAPIがモックになるため、E2Eでカバーする領域を明確にする",
            "KarmaはCIでヘッドレスChromeに依存するため、環境構築の自動化を忘れない",
            "builder切り替え時は`tsconfig.spec.json`のパスも更新する",
        ],
        related=[
            "Karma",
            "Jest",
            "Vitest",
        ],
    ),
    Entry(
        number=425,
        slug="webpack-vs-esbuild",
        title="Webpackビルダー vs Esbuild/Viteビルダー あなたはどっち派？",
        hook="ビルドシステム、伝統のWebpackベースを使い続ける？それともEsbuild/Viteにスイッチ？",
        overview="Angular v17でEsbuild＋Vite Dev Serverが導入され、`ng serve`挙動も選べます。",
        a_label="Webpackビルダー",
        a_prompt="Webpack派のメリットは？",
        a_answer="プラグイン・ローダー資産が豊富で、細かいカスタムも可能。レガシープロジェクトで安定しています。",
        a_pain="でも再ビルドが遅く、HMRも限定的…。",
        b_label="Esbuild/Vite",
        b_answer="Esbuildが高速にトランスパイルし、Vite Dev ServerでHMRがサクサク。プロダクションビルドも`ng build --builder esbuild`で高速化できます。",
        b_usecase="Esbuildにしたら`ng test`も`ng serve`も爆速になって開発が止まらない！",
        conclusion="カスタム優先ならWebpack、速度優先ならEsbuild/Vite。あなたはどっち派？",
        summary="Webpackは柔軟だがビルド速度が課題。Esbuild/Viteは制約はあるが高速でDXが良い。必要な拡張性とスピードで選ぶ。",
        goals=None,
        tech_points=None,
        code_a_title="Webpack派：従来のbuilder",
        code_a=dedent(
            """\
            "build": {
              "builder": "@angular-devkit/build-angular:browser",
              "options": { ... }
            }
            """
        ),
        code_b_title="Esbuild派：新builderを指定",
        code_b=dedent(
            """\
            "build": {
              "builder": "@angular-devkit/build-angular:browser-esbuild",
              "options": { ... }
            }
            """
        ),
        detail=dedent(
            """\
            // angular.json dev-server切り替え
            "serve": {
              "builder": "@angular-devkit/build-angular:dev-server",
              "options": { "buildTarget": "app:build:development-esbuild" }
            }
            """
        ),
        best_practices=[
            "Webpackビルダーを使う場合も`budget`/`namedChunks`など最適化オプションを定期的に見直す",
            "Esbuild導入時はPolyfillやグローバル変数の互換性を検証する",
            "CIでは両builderの成果物サイズを比較し、切り替え効果を可視化する",
        ],
        cautions=[
            "Esbuildは一部のWebpackプラグインが利用できないため代替策を検討する",
            "Webpack独自の`fileReplacements`等をEsbuildへ移行する際は設定位置が変わる",
            "Vite Dev Server使用時はプロキシ設定が変更されるのでAPI通信を確認する",
        ],
        related=[
            "Angular CLI builder",
            "Esbuild/Vite",
            "Webpack",
        ],
    ),
    Entry(
        number=426,
        slug="global-styles-vs-component-styles",
        title="global styles.scss vs Standalone Component styles あなたはどっち派？",
        hook="スタイル定義、`styles.scss`にまとめる？コンポーネントごとに閉じ込める？",
        overview="Standalone化でスタイル戦略も見直され、globalと局所のバランスが問われます。",
        a_label="global styles.scss",
        a_prompt="グローバル派の利点は？",
        a_answer="全ページ共通のトークンやリセットを1ファイルで管理でき、パージも楽。従来のAngular CLI構成とも互換です。",
        a_pain="でもコンポーネント固有のスタイルまでglobalに書くと衝突と回り込みが怖い…。",
        b_label="コンポーネントstyles",
        b_answer="Standalone Componentの`styleUrls`や`styles`に閉じ込めればスコープが限定され、CSSカスケードの意図が明確になります。",
        b_usecase="`standalone: true`で作るたびにスタイルが自給自足できて、globalファイルがスリムになった！",
        conclusion="トークンはglobal、実装はcomponentと役割分担しよう。あなたはどっち派？",
        summary="global stylesはテーマとベースルールに最適。Component stylesは局所スタイルを安全に適用できる。両者の境界を決める。",
        goals=None,
        tech_points=None,
        code_a_title="global派：`styles.scss`で宣言",
        code_a=dedent(
            """\
            :root {
              --primary: #22c55e;
            }
            body {
              font-family: 'Inter', sans-serif;
            }
            """
        ),
        code_b_title="component派：`styleUrls`へ閉じ込め",
        code_b=dedent(
            """\
            @Component({
              selector: 'app-card',
              standalone: true,
              styleUrls: ['./card.component.scss'],
            })
            export class CardComponent {}
            """
        ),
        detail=dedent(
            """\
            @Component({
              selector: 'app-card',
              standalone: true,
              styles: [
                `
                  :host {
                    display: block;
                    border: 1px solid var(--border, #e5e7eb);
                  }
                `,
              ],
            })
            export class CardComponent {}
            """
        ),
        best_practices=[
            "テーマトークンやリセットはglobal、UIパーツ固有スタイルはcomponent内に配置する",
            "CSS変数やSASS mixinを通じてglobalとcomponentを接続し、直接依存を減らす",
            "globalファイルの肥大化を防ぐためセクションごとにコメントや分割importを行う",
        ],
        cautions=[
            "component stylesでも`:host ::ng-deep`を乱用するとglobalと同じ状態になるので避ける",
            "globalスタイルに依存していることをREADME等に明記し、削除時の影響を把握する",
            "CSSの`@use`や`@forward`で循環参照を作らない",
        ],
        related=[
            "Angular CLI styles",
            "Scoped styles",
            "CSS設計",
        ],
    ),
    Entry(
        number=427,
        slug="subscribe-vs-tosignal",
        title="RxJS subscribeでUI同期 vs toSignalブリッジ あなたはどっち派？",
        hook="Observableの結果をUIに渡すとき、`.subscribe()`で代入？`toSignal`で変換？",
        overview="Signals登場でObservableとテンプレートの接続方法が増えました。",
        a_label="subscribe派",
        a_prompt="subscribeして代入する利点は？",
        a_answer="手元でデータを加工しやすく、古いコードとも相性抜群。`AsyncPipe`を使わなくても任意タイミングで更新できます。",
        a_pain="でも購読解除を忘れるとリークするし、`ChangeDetectorRef`を触ることも…。",
        b_label="toSignal派",
        b_answer="`toSignal(observable$, { initialValue })`でSignalへ変換でき、テンプレートでも`{{ data() }}`と呼べます。`takeUntilDestroyed`不要です。",
        b_usecase="`effect`に`toSignal`を渡すとコードの意図が明快になるね。",
        conclusion="一時的ならsubscribe、本格的にはtoSignalで統一するのがおすすめ。あなたはどっち派？",
        summary="subscribe代入は柔軟だがリークリスクがある。toSignalはSignalグラフに統合でき、UI同期が簡潔になる。",
        goals=None,
        tech_points=None,
        code_a_title="subscribe派：手動で値を保持",
        code_a=dedent(
            """\
            private readonly destroyRef = inject(DestroyRef);

            ngOnInit(): void {
              this.repo.list()
                .pipe(takeUntilDestroyed(this.destroyRef))
                .subscribe(items => (this.items = items));
            }
            """
        ),
        code_b_title="toSignal派：Signalへ変換",
        code_b=dedent(
            """\
            readonly items = toSignal(this.repo.list(), { initialValue: [] });

            template: `<li @for (item of items())>{{ item.name }}</li>`
            """
        ),
        detail=dedent(
            """\
            @Component({
              selector: 'app-hero-feed',
              standalone: true,
              templateUrl: './hero-feed.component.html',
            })
            export class HeroFeedComponent {
              private readonly repo = inject(HeroRepository);
              readonly heroes = toSignal(this.repo.list(), { initialValue: [] });
            }
            """
        ),
        best_practices=[
            "subscribe派でも`takeUntilDestroyed`や`AsyncPipe`で購読解除を自動化する",
            "`toSignal`を使う場合は`initialValue`を必ず渡し、テンプレート側でnullチェックを減らす",
            "Signalへの変換をサービス層で行い、コンポーネントはSignalのみ受け取る設計にすると移行が楽",
        ],
        cautions=[
            "`toSignal`は`cold` Observableでも購読するので副作用の再実行に注意",
            "subscribeとtoSignalを同じObservableで併用すると重複購読になる",
            "Signalsへ変換しても重い処理は`computed`でキャッシュし直す必要がある",
        ],
        related=[
            "toSignal/toObservable",
            "AsyncPipe",
            "takeUntilDestroyed",
        ],
    ),
    Entry(
        number=428,
        slug="ngcontent-vs-layout-component",
        title="ng-contentレイアウト vs Standalone Layoutコンポーネント あなたはどっち派？",
        hook="レイアウト、`ng-content`でスロットを切る？それとも専用レイアウトコンポーネントを作る？",
        overview="Angular もReact同様にslot構成が可能で、プロダクトによって書き味が変わります。",
        a_label="ng-content",
        a_prompt="ng-content派のメリットは？",
        a_answer="柔軟に子要素を挿入でき、既存DOMをそのまま包み込めます。コンテンツ数が変わるページに向きます。",
        a_pain="でも`<ng-content select>`が増えるとDOM構造が読みにくいし、Slotを跨いだ依存が追いづらい…。",
        b_label="Layoutコンポーネント",
        b_answer="`<app-dashboard-layout>`のようにPropsで明示的にセクションを渡すと、依存が型で表現されてレビューしやすいです。Standalone + Inputsで完結します。",
        b_usecase="`@Input() header!: TemplateRef`って明示しておくと、Slot漏れがすぐ分かる！",
        conclusion="柔軟性重視ならng-content、型安全重視ならLayoutコンポーネント。あなたはどっち派？",
        summary="ng-contentはシンプルで柔軟だが構造が暗黙的。LayoutコンポーネントはInputs/TemplateRefで受け取り、構造を明文化できる。",
        goals=None,
        tech_points=None,
        code_a_title="ng-content派：Slotで構成",
        code_a=dedent(
            """\
            <section class="shell">
              <header><ng-content select="[header]"></ng-content></header>
              <main><ng-content></ng-content></main>
            </section>
            """
        ),
        code_b_title="Layoutコンポーネント派：Inputsで渡す",
        code_b=dedent(
            """\
            @Component({
              selector: 'app-dashboard-layout',
              standalone: true,
              template: `
                <header><ng-container *ngTemplateOutlet="header"></ng-container></header>
                <main><ng-content></ng-content></main>
              `,
            })
            export class DashboardLayoutComponent {
              @Input({ required: true }) header!: TemplateRef<unknown>;
            }
            """
        ),
        detail=dedent(
            """\
            <app-dashboard-layout [header]="headerTpl">
              <p>content</p>
            </app-dashboard-layout>

            <ng-template #headerTpl>
              <h1>Title</h1>
            </ng-template>
            """
        ),
        best_practices=[
            "ng-contentを使う場合は`select`でスロットを明示し、使い方をドキュメント化する",
            "Layoutコンポーネントは`TemplateRef`や`Portal`をInputにし、可読性と型安全性を両立させる",
            "Slot構造の共通スタイルをglobalで管理しつつ、挿入する内容はcomponent styleで調整する",
        ],
        cautions=[
            "ng-contentは子要素のChangeDetection戦略に影響されるため、投影元と整合を取る",
            "Layoutコンポーネントを増やしすぎるとネストが深くなるので粒度を決める",
            "TemplateRefをInputにする場合はnullチェックを徹底する",
        ],
        related=[
            "Content Projection",
            "TemplateRef",
            "Standalone Layout",
        ],
    ),
    Entry(
        number=429,
        slug="cli-vs-nx",
        title="Angular CLI単体 vs Nx Workspace あなたはどっち派？",
        hook="モノレポ管理、純粋なAngular CLIで行く？Nxを導入する？",
        overview="大型プロジェクトではCLI単体とNxモノレポのどちらを選ぶかで開発体制が変わります。",
        a_label="Angular CLI単体",
        a_prompt="CLI派のメリットは？",
        a_answer="依存が少なく、`ng new`からそのままスタートできます。学習コストが低くアップグレードもシンプル。",
        a_pain="でも複数アプリやライブラリを束ねた瞬間にスクリプト管理が煩雑に…。",
        b_label="Nx Workspace",
        b_answer="NxはキャッシュやAffectedコマンドでCI時間を短縮し、Graphで依存可視化できます。モノレポガバナンスがかなり楽です。",
        b_usecase="Nxの`run-many --target=test`で影響範囲だけ実行できるの助かる！",
        conclusion="小規模ならCLI、大規模モノレポならNx。あなたはどっち派？",
        summary="Angular CLI単体は軽量で標準。Nxはモノレポ機能とタスク実行管理が強み。プロジェクト規模に応じて選定する。",
        goals=None,
        tech_points=None,
        code_a_title="CLI派：package.jsonで制御",
        code_a=dedent(
            """\
            {
              "scripts": {
                "start": "ng serve",
                "test": "ng test"
              }
            }
            """
        ),
        code_b_title="Nx派：project.jsonとタスクランナー",
        code_b=dedent(
            """\
            {
              "name": "app",
              "targets": {
                "serve": { "executor": "@nx/angular:dev-server" }
              }
            }
            """
        ),
        detail=dedent(
            """\
            npx create-nx-workspace@latest myorg --preset=angular-monorepo
            nx graph
            """
        ),
        best_practices=[
            "CLI運用でも`ng generate library`でコード共有を進め、いつでもNxに移行できるようにする",
            "Nx導入時はタスクキャッシュの保存先をCIと共有し、効果を最大化する",
            "モノレポのコードオーナーやlintルールをNxの`project.json`で明示する",
        ],
        cautions=[
            "Nxは設定ファイルが増えるため学習コストを見積もる",
            "CLIとNxのコマンドを混在させるとスクリプトが複雑になるのでラッパーを提供する",
            "モノレポでも依存境界が守られなければスケールしないのでタグベースlintを設定する",
        ],
        related=[
            "Angular CLI",
            "Nx Workspace",
            "Monorepo戦略",
        ],
    ),
    Entry(
        number=430,
        slug="eslint-vs-template-check",
        title="ESLint最小設定 vs ESLint+Templateチェック あなたはどっち派？",
        hook="Lint、TSだけ見る最小構成？HTMLテンプレまで静的解析する？",
        overview="Angular ESLintはテンプレートルールも提供しており、品質とコストのバランスを取る必要があります。",
        a_label="ESLint最小",
        a_prompt="最小構成派の利点は？",
        a_answer="TypeScript部分だけチェックするのでセットアップが簡単で、既存ルールセットを流用しやすいです。",
        a_pain="でもテンプレの`async`パイプや`trackBy`忘れなどは検出できない…。",
        b_label="Templateチェックあり",
        b_answer="`@angular-eslint/template`ルールを入れると、バインディングの型チェックやアクセシビリティ検査が可能。`ng g @angular-eslint/schematic:add-lint`で一括設定できます。",
        b_usecase="テンプレLintを入れたら未使用の`(click)`イベントを即発見できたよ！",
        conclusion="スピード優先なら最小、品質優先ならTemplateチェック込み。あなたはどっち派？",
        summary="ESLint最小構成は導入負荷が低いがUIの品質欠陥を見逃しがち。Template lintingは設定コストが上がるが、実行前に多くのバグを検出できる。",
        goals=None,
        tech_points=None,
        code_a_title="最小派：tsファイルのみlint",
        code_a=dedent(
            """\
            // .eslintrc.json
            {
              "extends": ["eslint:recommended", "plugin:@typescript-eslint/recommended"]
            }
            """
        ),
        code_b_title="Templateチェック派：HTMLも解析",
        code_b=dedent(
            """\
            {
              "overrides": [
                { "files": ["*.ts"], "extends": ["plugin:@angular-eslint/template/process-inline-templates"] },
                { "files": ["*.html"], "extends": ["plugin:@angular-eslint/template/recommended"] }
              ]
            }
            """
        ),
        detail=dedent(
            """\
            ng g @angular-eslint/schematics:add-linting --project app
            """
        ),
        best_practices=[
            "最小構成でも`@typescript-eslint`のstrictモードを有効にし、基礎品質を担保する",
            "Template lint導入後はCIでHTMLルール違反をブロックし、修正フローを定着させる",
            "false positiveが多いルールは理由を明記して無効化する",
        ],
        cautions=[
            "Template lintは実行時間が増えるため、差分Lintやキャッシュを活用する",
            "inline templateを使う場合は`process-inline-templates`を忘れず設定する",
            "プロジェクト固有の命名ルールをLintに組み込む際は共有ドキュメントを整備する",
        ],
        related=[
            "@angular-eslint",
            "ESLint",
            "Template Linting",
        ],
    ),
]


def render_daihon(entry: Entry) -> str:
    lines = [
        f"# #{entry.number} 「{entry.title}」台本",
        "",
        f"ずんだもん「{entry.hook}」",
        f"四国めたん「{entry.overview}」",
        f"ずんだもん「{entry.a_prompt}」",
        f"四国めたん「{entry.a_answer}」",
        f"ずんだもん「{entry.a_pain}」",
        f"四国めたん「{entry.b_answer}」",
        f"ずんだもん「{entry.b_usecase}」",
        f"四国めたん「{entry.conclusion}」",
    ]
    return "\n".join(lines) + "\n"


def render_document(entry: Entry) -> str:
    goal_items = entry.goals or [
        f"{entry.a_label}の構成と得意なシナリオを整理する",
        f"{entry.b_label}の採用メリットを理解する",
        "プロジェクト条件に応じた使い分け基準を決める",
    ]
    tech_items = entry.tech_points or [
        f"{entry.a_label}を成り立たせる主要API/構成要素",
        f"{entry.b_label}で押さえる設定やコード記述",
        "両者を共存・移行させるためのブリッジ手法",
    ]
    goals = "\n".join(f"- {goal}" for goal in goal_items)
    tech_points = "\n".join(f"- {point}" for point in tech_items)
    best = "\n".join(f"- {item}" for item in entry.best_practices)
    cautions = "\n".join(f"- {item}" for item in entry.cautions)
    related = "\n".join(f"- {item}" for item in entry.related)
    doc = f"""# #{entry.number} 「{entry.title}」

## 概要
{entry.summary}

## 学習目標
{goals}

## 技術ポイント
{tech_points}

## 📺 画面表示用コード（動画用）
**{entry.code_a_title}**
```typescript
{entry.code_a.strip()}
```

**{entry.code_b_title}**
```typescript
{entry.code_b.strip()}
```

## 💻 詳細実装例（学習用）
```typescript
{entry.detail.strip()}
```

## ベストプラクティス
{best}

## 注意点
{cautions}

## 関連技術
{related}
"""
    return doc


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    daihon_dir = base_dir / "daihon"
    doc_dir = base_dir / "document"
    daihon_dir.mkdir(parents=True, exist_ok=True)
    doc_dir.mkdir(parents=True, exist_ok=True)

    for entry in ENTRIES:
        daihon_path = daihon_dir / f"{entry.number:03d}_{entry.slug}.txt"
        doc_path = doc_dir / f"{entry.number:03d}_{entry.slug}.md"
        daihon_path.write_text(render_daihon(entry), encoding="utf-8")
        doc_path.write_text(render_document(entry), encoding="utf-8")
        print(f"Wrote #{entry.number} -> {daihon_path.name}")


if __name__ == "__main__":
    main()
