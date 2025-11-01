#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


DEFAULT_CODE = [
    """type Choice<A, B> = { current: A; alternative: B };""",
    """const poll = <T extends string>(label: T) => ({ label });""",
    """function vote<T>(value: T) {
  return value;
}""",
]

FEATURES: dict[str, dict[str, object]] = {
    "default": {
        "background": "最近のTypeScript v5.9でも{topic}の判断はチームごとに割れていますよね",
        "personal_duo": "ぼくは{option_a}寄りだけど、{option_b}派の気持ちもわかるんだよね",
        "personal_solo": "ぼくは{topic}はこうしてる派だけど、別のやり方も全然アリだと思ってるんだよね",
        "option_duo": "{option_a}にはメリットがあるし、{option_b}にも別の強みがあります。状況によって最適解が変わります",
        "option_solo": "{topic}にも利点とコストがあって、現場事情で判断が分かれますよね",
        "experience": "現場だと{topic}を巡って会議が長引いて、ガイドラインを書き直すイベントが発生するんだよ！",
        "cta_keyword": "{topic}の意見",
        "doc_keywords": "{topic}",
        "doc_notes": "テーマに対する賛否や運用方針をコメントで募る汎用テンプレート。",
        "doc_tone": "議論を歓迎する落ち着いたテンポ",
        "code": DEFAULT_CODE,
    },
    "interface_vs_type": {
        "background": "v5.9はユーティリティ型が充実したので{topic}も改めて選び直す時期ですね",
        "personal_duo": "ぼくは{option_a}でドメインモデルを書く派だけど、DTOは{option_b}でまとめたいんだよね",
        "option_duo": "{option_a}は宣言マージや継承が得意、一方{option_b}はユニオンや条件型が柔軟です",
        "experience": "現場だと{option_a}と{option_b}を巡るレビュー合戦が始まって、命名規則ドキュメントが増刷されるんだよ！",
        "cta_keyword": "interfaceかtypeか",
        "doc_keywords": "`interface`, `type alias`, 宣言マージ",
        "doc_notes": "派閥と使い分けルールをコメントで募る。",
        "doc_tone": "派閥トークを軽快に煽るテンポ",
        "code": [
            """interface User {
  id: string;
  name: string;
}""",
            """type UserSummary = Pick<User, "id" | "name">;""",
            """type ApiResult<T> = { data: T } | { error: string };""",
        ],
    },
    "satisfies_usage": {
        "background": "`satisfies`はリテラル推論を崩さず構造チェックできるので{topic}の議論が熱いですよね",
        "personal_duo": "ぼくは{option_a}で静的保証を固めたい派だけど、緊急対応では{option_b}の柔軟さに甘えたくなるんだよね",
        "option_duo": "{option_a}は余計なプロパティを弾ける安心感、{option_b}は記述量が少なくスピード重視なところが魅力です",
        "experience": "現場だと`satisfies`を入れた瞬間に警告が噴出して、棚卸し会議が始まるんだよ！",
        "cta_keyword": "satisfies運用",
        "doc_keywords": "`satisfies`, リテラル保持, 型検証",
        "doc_notes": "`satisfies`導入の可否や運用ルールをコメントで募る。",
        "doc_tone": "慎重派と攻め派を仲裁するテンポ",
        "code": [
            """const config = {
  mode: "strict",
  retries: 2,
} satisfies {
  mode: "strict" | "relaxed";
  retries: number;
};""",
            """const loose = {
  mode: "strict",
  retries: 2,
} as {
  mode: "strict" | "relaxed";
  retries: number;
};""",
            """type Mode = typeof config.mode;""",
        ],
    },
    "any_policy": {
        "background": "`noImplicitAny`やlintの扱いは{topic}でも人によって温度差がありますね",
        "personal_duo": "ぼくは{option_a}寄りで徹底したい派だけど、締め切り前になると{option_b}に逃げたくなるんだよね",
        "option_duo": "{option_a}だと安全だけどコストが高く、{option_b}は速いけれどバグの温床になることもあります",
        "experience": "現場だと`any`を巡る議論で朝会が延長して、結局ルール文書を改訂するんだよ！",
        "cta_keyword": "anyルール",
        "doc_keywords": "`any`, lint, 運用方針",
        "doc_notes": "`any`許容ラインと運用体制を共有してもらう。",
        "doc_tone": "自虐混じりに議論を引き出す",
        "code": [
            """function unsafe(value: any) {
  return value;
}""",
            """function safe(value: unknown) {
  if (typeof value === "string") return value.toUpperCase();
  return value;
}""",
            """type Cleaner<T> = (value: T) => void;""",
        ],
    },
    "strict_null": {
        "background": "`strictNullChecks`をいつONにするかは{topic}でも悩ましいですね",
        "personal_solo": "ぼくは早めにON派だけど、レガシー移行だと一気にやる勇気が出ないんだよね",
        "option_solo": "ONにするとnullバグが早期に見つかる一方、移行コストは確かに高いです",
        "experience": "現場だとONに切り替えた週はビルドが真っ赤になって、null駆除合宿が開催されるんだよ！",
        "cta_keyword": "strictNullChecks移行",
        "doc_keywords": "`strictNullChecks`, null安全",
        "doc_notes": "移行計画や段階的導入のコツをコメントで募る。",
        "doc_tone": "移行の痛みを共有する柔らかいテンポ",
        "code": [
            """type User = {
  id: string;
  email?: string | null;
};""",
            """function ensureEmail(user: User) {
  if (!user.email) throw new Error("email required");
  return user.email.toLowerCase();
}""",
            """const draft: User = { id: "u1" };""",
        ],
    },
    "unknown_vs_any": {
        "background": "{topic}の境界線はv5.9でも議論が終わりませんね",
        "personal_duo": "ぼくは{option_a}で受けて段階的に絞る派だけど、締め切り前は{option_b}に逃げたくなるんだよね",
        "option_duo": "{option_a}は安全だけどガードを書く手間が増え、{option_b}は早いけれどバグが潜みます",
        "experience": "現場だとAPIの責任分界線で火花が散って、結局合同レビューになるんだよ！",
        "cta_keyword": "unknownかanyか",
        "doc_keywords": "`unknown`, `any`, 型ガード",
        "doc_notes": "どこで`unknown`に変換し、どこで`any`を許容するかの運用を共有。",
        "doc_tone": "安全志向とスピード志向の温度差を面白がる",
        "code": [
            """function isUser(value: unknown): value is { id: string } {
  return typeof value === "object" && value !== null && "id" in value;
}""",
            """const payload: unknown = JSON.parse('{"id":"u1"}');""",
            """if (isUser(payload)) {
  console.log(payload.id);
}""",
        ],
    },
    "as_const": {
        "background": "`as const`はリテラル推論を守れるので{topic}の答えが気になるところです",
        "personal_solo": "ぼくは設定オブジェクトには全部付けたい派だけど、書きすぎると読みづらいって言われるんだよね",
        "option_solo": "`as const`で推論が崩れない安心感と、柔軟に変更したいときの邪魔さのバランスが難しいです",
        "experience": "現場だと付け忘れた箇所で型が崩れて、`git blame`大会が始まることもあるんだよ！",
        "cta_keyword": "asconst運用",
        "doc_keywords": "`as const`, リテラル型",
        "doc_notes": "どこまで徹底するかの基準をコメントで募る。",
        "doc_tone": "小ネタを畳みかけるテンポ",
        "code": [
            """const roles = ["admin", "editor"] as const;""",
            """type Role = (typeof roles)[number];""",
            """const config = {
  mode: "dark",
  retries: 3,
} as const;""",
        ],
    },
    "enum_literal": {
        "background": "`enum`とリテラルユニオン、{topic}の好みは分かれますね",
        "personal_duo": "ぼくはフロントでは{option_b}派だけど、サーバーでは{option_a}を使いたくなるんだよね",
        "option_duo": "{option_a}はメンバーアクセスが楽で、{option_b}は型操作やtree-shakingがしやすいです",
        "experience": "現場だと`enum`禁止ルールを出したら他チームから抗議が来る事件があるんだよ！",
        "cta_keyword": "enumかliteralか",
        "doc_keywords": "`enum`, リテラルユニオン",
        "doc_notes": "採用可否と基準をコメントで集めたい。",
        "doc_tone": "派閥バトルを楽しく演出",
        "code": [
            """enum RoleEnum {
  Admin = "admin",
  Editor = "editor",
}""",
            """const RoleLiteral = ["admin", "editor"] as const;
type Role = (typeof RoleLiteral)[number];""",
            """function label(role: Role) {
  return role === "admin" ? "管理者" : "編集";
}""",
        ],
    },
    "readonly": {
        "background": "`readonly`プロパティの徹底度は{topic}でも意見が割れますね",
        "personal_solo": "ぼくはドメイン層は`readonly`派だけど、UIでは柔軟に書き換えたくなるんだよね",
        "option_solo": "`readonly`で守る安心感と、更新が必要な場面での柔軟さのどちらを優先するかがポイントです",
        "experience": "現場だと`readonly`を忘れて誰かが`push`してしまい、git blameが火を噴くんだよ！",
        "cta_keyword": "readonly運用",
        "doc_keywords": "`readonly`, イミュータブル設計",
        "doc_notes": "値オブジェクトやDTOでの扱いをコメントで共有。",
        "doc_tone": "イミュータブル信者と現場派の温度差を軽快に描く",
        "code": [
            """type User = { id: string; tags: string[] };""",
            """type FrozenUser = Readonly<User>;""",
            """type Mutable<T> = {
  -readonly [K in keyof T]: T[K];
};""",
        ],
    },
    "infer_mastery": {
        "background": "`infer`は条件型の肝で、{topic}でも習熟度が問われますね",
        "personal_solo": "ぼくは最近ようやく`infer`に慣れてきた派だけど、ネストするとすぐ迷子になるんだよね",
        "option_solo": "`infer`に慣れると型ヘルパーが増やせますが、読みやすさのケアが課題です",
        "experience": "現場だと`infer`入りのPRが来るとレビューで『読めません』スタンプが押される事件が起きるんだよ！",
        "cta_keyword": "infer習熟度",
        "doc_keywords": "`infer`, 条件型",
        "doc_notes": "学習のコツや参考資料をコメントで共有してもらう。",
        "doc_tone": "学習談義を盛り上げる",
        "code": [
            """type ExtractReturn<T> = T extends (...args: any[]) => infer R ? R : never;""",
            """type Handler = (value: number) => Promise<string>;
type Result = ExtractReturn<Handler>;""",
            """type ExtractArray<T> = T extends (infer U)[] ? U : never;""",
        ],
    },
    "partial_pick": {
        "background": "`Partial`や`Pick`をどこまで使うかは{topic}でもよく議論になりますね",
        "personal_duo": "ぼくは純正ユーティリティで乗り切りたい派だけど、自作型の便利さもわかるんだよね",
        "option_duo": "{option_a}は手軽だけど複雑な要件では限界があり、{option_b}は柔軟だけどメンテが大変です",
        "experience": "現場だと`DeepPartial`を持ち込んだ瞬間に型が爆発して、`tsc`が叫ぶんだよ！",
        "cta_keyword": "Partial運用",
        "doc_keywords": "`Partial`, `Pick`, DTO",
        "doc_notes": "純正派・自作派それぞれのプラクティスをコメントで募る。",
        "doc_tone": "組み立て作業あるあるをコミカルに",
        "code": [
            """type User = { id: string; name: string; role: "admin" | "editor" };""",
            """type UpdateUser = Partial<Pick<User, "name" | "role">>;""",
            """type DeepPartial<T> = { [K in keyof T]?: DeepPartial<T[K]> };""",
        ],
    },
    "type_predicate": {
        "background": "ユーザー定義型ガードは{topic}でも注目されるテクニックですね",
        "personal_solo": "ぼくは`is`を書いて安心したい派だけど、テストを書かないと信用してもらえないんだよね",
        "option_solo": "型ガードを自作すると表現力が上がる反面、実装ミスすると逆に危険というジレンマがあります",
        "experience": "現場だと型ガードの置き場と命名で議論が起きて、ヘルパー棚卸し会議が開かれるんだよ！",
        "cta_keyword": "typeガード運用",
        "doc_keywords": "型ガード, `is`述語",
        "doc_notes": "型ガードの共有方法やテスト観点をコメントで募る。",
        "doc_tone": "慎重派と攻め派の議論を促す",
        "code": [
            """function isUser(value: unknown): value is { id: string } {
  return typeof value === "object" && value !== null && "id" in value;
}""",
            """function handle(value: unknown) {
  if (isUser(value)) {
    return value.id;
  }
  throw new Error("not user");
}""",
            """type Guard<T> = (value: unknown) => value is T;""",
        ],
    },
    "nonnullable": {
        "background": "`NonNullable`をどこまで義務化するかは{topic}でも悩ましいですね",
        "personal_solo": "ぼくはAPIレスポンスを受け取ったら即`NonNullable`したい派だけど、書きすぎると読みにくいんだよね",
        "option_solo": "`NonNullable`でnullを弾くと安全ですが、リファインを忘れると逆に危険という声もあります",
        "experience": "現場だと`NonNullable`不足を炙り出すバグハントが定期的に開催されるんだよ！",
        "cta_keyword": "NonNullable運用",
        "doc_keywords": "`NonNullable`, null排除",
        "doc_notes": "どのレイヤーで`NonNullable`するかをコメントで共有してもらう。",
        "doc_tone": "安全志向の会話をテンポ良く",
        "code": [
            """type MaybeUser = { id: string; email: string | null };""",
            """type StrictUser = { id: string; email: NonNullable<string | null> };""",
            """function ensureEmail(user: MaybeUser) {
  if (!user.email) throw new Error("missing email");
  return user.email;
}""",
        ],
    },
    "async_return": {
        "background": "非同期戻り値の扱いは{topic}でも議論が尽きませんね",
        "personal_solo": "ぼくは`Awaited`で型を抜き出す派だけど、意図しないユニオンになると焦るんだよね",
        "option_solo": "明示的に書く安心感と、推論に任せるスピード感のバランスが難しいです",
        "experience": "現場だと`Promise.all`の型レビューで会議が30分延長する事件が起こるんだよ！",
        "cta_keyword": "async戻り型",
        "doc_keywords": "Promise, `Awaited`, 戻り値",
        "doc_notes": "戻り値管理のテクニックをコメントで教えてもらう。",
        "doc_tone": "非同期あるあるを軽快に",
        "code": [
            """async function fetchUser() {
  return { id: "1", name: "m" };
}""",
            """type UserPromise = ReturnType<typeof fetchUser>;
type User = Awaited<UserPromise>;""",
            """async function load() {
  const user: User = await fetchUser();
  return user.name;
}""",
        ],
    },
    "result_pattern": {
        "background": "Result型はエラーハンドリングの定番で、{topic}でも採用可否が議論になりますね",
        "personal_solo": "ぼくはドメイン層だけResult派だけど、UIでは例外に頼りたくなるんだよね",
        "option_solo": "Resultは明示的で安全、例外はコード量が少なく直感的というトレードオフです",
        "experience": "現場だとResult導入提案が出るたびに賛成派と反対派で長期戦になるんだよ！",
        "cta_keyword": "Result導入状況",
        "doc_keywords": "Result型, 判別ユニオン",
        "doc_notes": "Result導入の判断と実例をコメントで募る。",
        "doc_tone": "設計議論を穏やかにファシリテート",
        "code": [
            """type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };""",
            """function success<T>(value: T): Result<T, never> {
  return { ok: true, value };
}""",
            """function failure<E>(error: E): Result<never, E> {
  return { ok: false, error };
}""",
        ],
    },
    "tsconfig_strict": {
        "background": "`tsconfig`のstrict関連は{topic}でも判断が分かれますね",
        "personal_solo": "ぼくは全部ON派だけど、レガシー移行では段階的に外したくなるんだよね",
        "option_solo": "strictを全ONにすると安全ですが、警告の山に耐える覚悟が必要です",
        "experience": "現場だとstrictを巡る棚卸し会議が始まって、tsconfigファイルが増殖するんだよ！",
        "cta_keyword": "strict設定方針",
        "doc_keywords": "`tsconfig`, strict",
        "doc_notes": "strictフラグのON/OFF基準と移行手順をコメントで共有してもらう。",
        "doc_tone": "設定談議を落ち着いて進行",
        "code": [
            """// tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true
  }
}""",
            """// tsconfig.relaxed.json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "strictNullChecks": false
  }
}""",
            """type StrictMode = {
  strict: boolean;
};""",
        ],
    },
    "module_resolution": {
        "background": "`moduleResolution`は{topic}でもプロジェクトによって答えが違いますね",
        "personal_duo": "ぼくはフロントは{option_a}派だけど、ライブラリは{option_b}の方が安心なんだよね",
        "option_duo": "{option_a}は最新ツールとの相性が良く、{option_b}は従来構成との互換性が魅力です",
        "experience": "現場だと設定差分で補完が暴れて、tsconfigの分割メンテが始まるんだよ！",
        "cta_keyword": "moduleResolution選択",
        "doc_keywords": "`moduleResolution`, bundler, node",
        "doc_notes": "採用理由と注意点をコメントで共有してもらう。",
        "doc_tone": "設定談義をカジュアルに",
        "code": [
            """// tsconfig.web.json
{
  "compilerOptions": {
    "moduleResolution": "bundler"
  }
}""",
            """// tsconfig.node.json
{
  "compilerOptions": {
    "moduleResolution": "node"
  }
}""",
            """import path from "node:path";""",
        ],
    },
    "paths_alias": {
        "background": "`paths`エイリアスは{topic}でも便利さとメンテコストの両立が課題ですね",
        "personal_solo": "ぼくは`@/`でまとめる派だけど、深い階層では相対パスに戻したくなるんだよね",
        "option_solo": "エイリアスは読みやすいけれど設定が増え、相対パスはシンプルだけど長くなりがちです",
        "experience": "現場だとpathsの同期漏れでCIが真っ赤になって、設定ファイルの棚卸しが始まるんだよ！",
        "cta_keyword": "paths運用",
        "doc_keywords": "`paths`, インポートエイリアス",
        "doc_notes": "paths設定の同期方法や命名規則をコメントで募る。",
        "doc_tone": "現場の苦労を軽く笑うテンポ",
        "code": [
            """// tsconfig.json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  }
}""",
            """import { handler } from "@/features/user/handler";""",
            """import { helper } from "../shared/helper";""",
        ],
    },
    "isolated_modules": {
        "background": "`isolatedModules`はESM互換を意識するなら外せない設定で、{topic}の判断が悩ましいですね",
        "personal_solo": "ぼくはビルド互換のためON派だけど、テスト環境ではOFFにしたくなるんだよね",
        "option_solo": "ONにするとファイル単位で安全になりますが、`export type`漏れとの戦いが始まります",
        "experience": "現場だとONに切り替えた瞬間に型の再エクスポートが怒られて、深夜に修正祭りが開かれるんだよ！",
        "cta_keyword": "isolatedModules運用",
        "doc_keywords": "`isolatedModules`, ESM互換",
        "doc_notes": "ON/OFFの理由や運用での注意点をコメントで募る。",
        "doc_tone": "設定トラブルをネタにするテンポ",
        "code": [
            """// tsconfig.json
{
  "compilerOptions": {
    "isolatedModules": true
  }
}""",
            """export type User = {
  id: string;
};""",
            """export const createUser = (id: string): User => ({ id });""",
        ],
    },
    "no_unchecked": {
        "background": "`noUncheckedIndexedAccess`は配列アクセスへundefinedを含めるので、{topic}で議論が盛り上がりますね",
        "personal_solo": "ぼくはデータ整形層ではON派だけど、UIでは冗長になってOFFにしたくなるんだよね",
        "option_solo": "ONにすると安全ですが、オプショナルチェーンが増えて読みづらさとの戦いもあります",
        "experience": "現場だとONにした瞬間に`?.`だらけになって、命名リファクタが始まるんだよ！",
        "cta_keyword": "noUnchecked設定",
        "doc_keywords": "`noUncheckedIndexedAccess`, null安全",
        "doc_notes": "どの層でON/OFFするかをコメントで共有してもらう。",
        "doc_tone": "安全志向の悩みを共感",
        "code": [
            """// tsconfig.json
{
  "compilerOptions": {
    "noUncheckedIndexedAccess": true
  }
}""",
            """const list: string[] = ["ts", "js"];""",
            """const first = list[0]?.toUpperCase();""",
        ],
    },
    "verbatim": {
        "background": "`verbatimModuleSyntax`は`import type`を最適化してくれるので、{topic}の採否が注目ですね",
        "personal_solo": "ぼくは将来のESM互換のためON派だけど、古いコードで怒られるとOFFに戻したくなるんだよね",
        "option_solo": "ONで型だけのimportが自動整理されるメリットと、書き方を変えるコストのバランスが難しいです",
        "experience": "現場だとONにした途端`import type`漏れでCIが真っ赤になって、リファクタ合戦が始まるんだよ！",
        "cta_keyword": "verbatim設定",
        "doc_keywords": "`verbatimModuleSyntax`, `import type`",
        "doc_notes": "切り替えた/していない理由とコツをコメントで募る。",
        "doc_tone": "設定アップデート談を共有",
        "code": [
            """// tsconfig.json
{
  "compilerOptions": {
    "verbatimModuleSyntax": true
  }
}""",
            """import type { User } from "./types";""",
            """import { createUser } from "./factory";""",
        ],
    },
    "module_target": {
        "background": "`module`ターゲットの選択は{topic}でも環境依存ですね",
        "personal_duo": "ぼくはブラウザは{option_a}派だけど、Nodeでは{option_b}に戻りたくなるんだよね",
        "option_duo": "{option_a}は最新構文とtree-shakingが強み、{option_b}は互換性と既存ツールの安心感があります",
        "experience": "現場だとターゲットを切り替えたら`require`が怒って、深夜に設定を差し戻す事件が起きるんだよ！",
        "cta_keyword": "module設定",
        "doc_keywords": "`module`, ESM, CJS",
        "doc_notes": "デプロイ環境別の設定方針をコメントで共有してもらう。",
        "doc_tone": "デプロイ現場の悩みを共有",
        "code": [
            """// tsconfig.esm.json
{
  "compilerOptions": {
    "module": "esnext"
  }
}""",
            """// tsconfig.cjs.json
{
  "compilerOptions": {
    "module": "commonjs"
  }
}""",
            """export const echo = (value: string) => value;""",
        ],
    },
    "decorators": {
        "background": "デコレータはStage 3到達で{topic}の判断が改めて問われていますね",
        "personal_duo": "ぼくは本番コードでは{option_a}派だけど、レガシー対応のため{option_b}も捨てられないんだよね",
        "option_duo": "{option_a}は公式仕様で将来性があり、{option_b}はメタデータ互換で安心感があります",
        "experience": "現場だと切り替えた瞬間にビルドが怒って、metadata周りを総見直しすることがあるんだよ！",
        "cta_keyword": "decorator運用",
        "doc_keywords": "デコレータ, Stage 3, `experimentalDecorators`",
        "doc_notes": "正式採用/従来構文の使い分けをコメントで共有。",
        "doc_tone": "慎重派と歓迎派の温度差を演出",
        "code": [
            """function Log(prefix: string) {
  return function (
    _target: unknown,
    _propertyKey: string | symbol,
    descriptor: PropertyDescriptor,
  ) {
    const fn = descriptor.value as Function;
    descriptor.value = function (...args: unknown[]) {
      console.log(prefix, args);
      return fn.apply(this, args);
    };
  };
}""",
            """class Service {
  @Log("call")
  run() {
    return "ok";
  }
}""",
            """new Service().run();""",
        ],
    },
    "ts_runner": {
        "background": "`ts-node`と`tsx`/esbuildの選択は{topic}でも分かれるポイントですね",
        "personal_duo": "ぼくはローカルは{option_a}派だけど、CIは{option_b}で整えたくなるんだよね",
        "option_duo": "{option_a}は互換性が高く、{option_b}は起動が速いという違いがあります",
        "experience": "現場だと実行コマンドが環境ごとに違って、ドキュメント整備が大仕事になるんだよ！",
        "cta_keyword": "ts実行環境",
        "doc_keywords": "`ts-node`, `tsx`, esbuild",
        "doc_notes": "ローカル/CIの使い分けとトラブルをコメントで共有してもらう。",
        "doc_tone": "ツール選定談義を軽妙に",
        "code": [
            """// package.json
{
  "scripts": {
    "dev:ts-node": "ts-node --esm src/index.ts",
    "dev:tsx": "tsx src/index.ts"
  }
}""",
            """import { readFileSync } from "node:fs";""",
            """console.log(readFileSync("package.json", "utf8").length);""",
        ],
    },
    "esbuild": {
        "background": "esbuildで型チェックを省略する運用は{topic}でも賛否が分かれますね",
        "personal_duo": "ぼくは開発中は{option_a}派だけど、最終的には{option_b}を走らせたくなるんだよね",
        "option_duo": "{option_a}は速いけれど型チェックが抜け、{option_b}は安心だけど遅いというジレンマです",
        "experience": "現場だと『チェックはCIで』と割り切ったら、ローカルで見逃した型バグが本番寸前まで行く事件があるんだよ！",
        "cta_keyword": "esbuild運用",
        "doc_keywords": "esbuild, `tsc --noEmit`",
        "doc_notes": "型検査をどこで走らせるかの運用をコメントで共有。",
        "doc_tone": "スピード vs 安全の議論を促す",
        "code": [
            """// package.json
{
  "scripts": {
    "build": "esbuild src/index.ts --bundle --outfile=dist/app.js",
    "typecheck": "tsc --noEmit"
  }
}""",
            """import { createServer } from "node:http";""",
            """createServer((_req, res) => {
  res.end("ok");
}).listen(3000);""",
        ],
    },
}

DEFAULT_FEATURE = FEATURES["default"]

KEYWORD_FEATURE_MAP: list[tuple[list[str], str]] = [
    (["interface", "命名規則"], "interface_vs_type"),
    (["satisfies"], "satisfies_usage"),
    ([" any", "`any`", "any`", "any "], "any_policy"),
    (["strictnullchecks"], "strict_null"),
    (["unknown", "nonnullable"], "unknown_vs_any"),
    (["as const"], "as_const"),
    (["enum", "literal union"], "enum_literal"),
    (["readonly", "mutable"], "readonly"),
    (["infer", "variadic tuple"], "infer_mastery"),
    (["partial", "pick", "deeppartial", "utility-types"], "partial_pick"),
    (["type predicate"], "type_predicate"),
    (["nonnullable"], "nonnullable"),
    (["async", "promise", "awaited"], "async_return"),
    (["result"], "result_pattern"),
    (["strict "], "tsconfig_strict"),
    (["moduleresolution"], "module_resolution"),
    (["paths"], "paths_alias"),
    (["isolatedmodules"], "isolated_modules"),
    (["nouncheckedindexedaccess"], "no_unchecked"),
    (["verbatimmodule"], "verbatim"),
    (["module "], "module_target"),
    (["decorator"], "decorators"),
    (["ts-node", "tsx"], "ts_runner"),
    (["esbuild"], "esbuild"),
]


def parse_titles(path: Path) -> list[str]:
    pattern = re.compile(r"^\s*\d+\.\s+「(.+)」")
    titles: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            titles.append(match.group(1))
    return titles


def choose_feature(question: str) -> dict[str, object]:
    lower = question.lower()
    for keywords, feature_id in KEYWORD_FEATURE_MAP:
        if any(keyword in lower for keyword in keywords):
            return FEATURES.get(feature_id, DEFAULT_FEATURE)
    return DEFAULT_FEATURE


def split_segments(question: str) -> list[str]:
    return [seg.strip() for seg in re.split(r"[？?]", question) if seg.strip()]


def render(template: str, context: dict[str, str]) -> str:
    return template.format(**context)


def build_dialogues(question: str, feature: dict[str, object]) -> tuple[list[str], str, str, str, str, str]:
    segments = split_segments(question)
    primary = segments[0] if segments else question
    option_a = segments[0] if segments else primary
    option_b = segments[1] if len(segments) > 1 else "別の選択肢"
    context = {
        "question": question,
        "topic": primary,
        "option_a": option_a,
        "option_b": option_b,
    }

    background = render(feature.get("background", DEFAULT_FEATURE["background"]), context)
    if len(segments) > 1:
        personal_template = feature.get("personal_duo", DEFAULT_FEATURE["personal_duo"])
        option_template = feature.get("option_duo", DEFAULT_FEATURE["option_duo"])
    else:
        personal_template = feature.get("personal_solo", DEFAULT_FEATURE["personal_solo"])
        option_template = feature.get("option_solo", DEFAULT_FEATURE["option_solo"])
    personal = render(personal_template, context)
    option_line = render(option_template, context)
    experience = render(feature.get("experience", DEFAULT_FEATURE["experience"]), context)
    cta_keyword = render(feature.get("cta_keyword", DEFAULT_FEATURE["cta_keyword"]), context)

    dialogues = [
        f"ずんだもん「{question}」",
        f"四国めたん「{background}」",
        f"ずんだもん「{personal}」",
        f"四国めたん「{option_line}」",
        f"ずんだもん「{experience}」",
        f"四国めたん「みなさんはどうしていますか？コメントで“{cta_keyword}”って教えてください！」",
        "ずんだもん「理由も添えてくれたら嬉しいな！」",
    ]

    doc_keywords = render(feature.get("doc_keywords", DEFAULT_FEATURE["doc_keywords"]), context)
    doc_notes = render(feature.get("doc_notes", DEFAULT_FEATURE["doc_notes"]), context)
    doc_tone = feature.get("doc_tone", DEFAULT_FEATURE["doc_tone"])

    code_snippets = feature.get("code", DEFAULT_FEATURE["code"])
    code_block = "\n\n".join(snippet.rstrip() for snippet in code_snippets)

    return dialogues, code_block, doc_keywords, doc_notes, cta_keyword, doc_tone


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    title_path = base_dir.parent / "viewer-question-titles.md"
    daihon_dir = base_dir / "daihon"
    document_dir = base_dir / "document"

    titles = parse_titles(title_path)
    if not titles:
        raise SystemExit("タイトルが見つかりませんでした。")

    daihon_dir.mkdir(parents=True, exist_ok=True)
    document_dir.mkdir(parents=True, exist_ok=True)

    for index, question in enumerate(titles, start=1):
        feature = choose_feature(question)
        (
            dialogues,
            code_block,
            doc_keywords,
            doc_notes,
            cta_keyword,
            doc_tone,
        ) = build_dialogues(question, feature)

        daihon_path = daihon_dir / f"{index:03}.txt"
        document_path = document_dir / f"{index:03}.md"

        daihon_path.write_text("\n".join(dialogues) + "\n", encoding="utf-8")

        doc_lines = [
            f"# #{index:03} 「{question}」制作ドキュメント",
            "",
            "## 台本",
            *dialogues,
            "",
            "## 画面表示用コード",
            "",
            "```typescript",
            code_block,
            "```",
            "",
            "## 制作メモ",
            f"- **問いの切り口**: {question}",
            "- **想定視聴者層**: TypeScriptの設計やルール決めで悩むエンジニア",
            f"- **押さえる技術キーワード**: {doc_keywords}",
            "- **キャラの立場**: 四国めたん=整理役 / ずんだもん=実装現場の迷いを代弁",
            f"- **コメントで聞きたいこと**: {cta_keyword}",
            f"- **補足メモ**: {doc_notes}",
            f"- **進行トーン**: {doc_tone}",
            "",
        ]

        document_path.write_text("\n".join(doc_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
